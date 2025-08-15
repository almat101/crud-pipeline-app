import logging
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import re
from datetime import datetime

#### MONGO DB connection creation ####
client = MongoClient("mongodb://localhost:27017/")
db = client["products_db"]
collection = db["raw_products"]


#SCRAPE_URL= "https://www.subito.it/annunci-italia/vendita/elettronica/?q=thinkpad+t14"
SCRAPE_URL="https://www.subito.it/annunci-italia/vendita/elettronica/?q=iphone+15"
PRODUCT_NAME="iphone 15"
UNWANTED_LIST= ["cover","case","protezione","custodia"]
SELECTOR_PRODUCTS = "a.SmallCard-module_link__hOkzY"
#SELECTOR_PRODUCTS = "div.SmallCard-module_upper-data-group__aRFDu"
SELECTOR_TITLE = "h2.headline-6.ItemTitle-module_item-title__VuKDo"
SELECTOR_CITY = "div.PostingTimeAndPlace-module_date-location__1Owcv span"
SELECTOR_PROVINCE = "div.PostingTimeAndPlace-module_date-location__1Owcv span.caption.small.city"
SELECTOR_PRICE = "div.index-module_price-group__B9-pV p.index-module_price__N7M2x"

app = FastAPI()

# Configure logging to display messages at the INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger instance for this module


@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}


@app.get("/scrape")
def scrape():
    try:
        logger.info("selenium driver start..")
        # Initialize the Selenium WebDriver and navigate to the target URL
        driver = setup()

        # Get the title of the current webpage
        title = driver.title

        # Set an implicit wait time of 5 seconds for finding elements
        driver.implicitly_wait(5)

        # find all elements matching the css selector (changed to take the DIV father element)
        products = driver.find_elements(By.CSS_SELECTOR, SELECTOR_PRODUCTS)

        if not products:
            logger.warning("No products found on the page. Check the CSS selector or page structure.")
            return {"message": "No products found", "result": []}

        raw_data = []
        for product in products:
            try:
                #Selenium is executing js to extract the title from css query selector using . to connect class name
                title = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_TITLE}')?.textContent || '';", product)
                city = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_CITY}')?.textContent || '';", product)
                province = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_PROVINCE}')?.textContent || '';", product)
                price = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_PRICE}')?.textContent || '';", product)
                url = product.get_attribute("href")
                # price_html = driver.execute_script("return arguments[0].outerHTML;", product)
                # logger.info(f"Price HTML: {price_html}")

                product_data = {
                    "title": title.strip(),
                    "city": city.strip(),
                    "province": province.strip(),
                    "price": price.strip(),
                    "shipping_available": False,
                    "date_scraped": None,
                    "url": url
                }
                raw_data.append(product_data)

            except Exception as e:
                # Log the error for this product and continue with the next one
                logger.error(f"Error scraping product: {e}")
                continue

        # Close the browser and clean up resources moved to finally block 
        #teardown(driver)

        # Log a message indicating the scraping process was completed successfully
        logger.info(f"Scraping completed succesfully: {raw_data}")

        return saving_data(raw_data)

    except Exception as e:
        logger.error(f"Error during scrape: {e}")
        return {"message": "scrape failed", "error" : str(e)}
    finally:
        #teardown here to always cleanup browser driver
        if(driver):
            teardown(driver)

def setup():
    try:
        # Initialize the Selenium WebDriver (Chrome) and navigate to the target URL
        driver = webdriver.Chrome()
        driver.get(SCRAPE_URL)
        return driver  # Return the WebDriver instance
    except Exception as e:
        logger.error(f"Error on setup webdriver: {e}")
        raise # Re-raises the same exception


def teardown(driver):
    try:
        # Quit the WebDriver and close the browser
        driver.quit()
    except Exception as e:
        logger.error(f"Error during WebDriver teardown: {e}")

#implementazione pulizia e salvataggio dati in mongo db
def saving_data(raw_data): 
    try:
        cleaned_data = []
        ### delete all elements in the collections
        collection.delete_many({})
        for product in raw_data:
            filter_query = {"title": product["title"]}  # This finds a document with the same title
            update_statement = {"$set": product}       # This sets all fields to the new data
            ###title
            product['title'] = product['title'].lower()
            #logger.info(f"product title is: {product['title']}")
            #filer product that does not contain product_name in product_title
            if not(PRODUCT_NAME in product['title']):
                logger.info(f"skip the product does not contain {PRODUCT_NAME} in {product['title']}")
                continue
            #looping on a list of unwanted names, if one name is found in the product_title skip the product
            skip_product = False
            for unwanted_product in UNWANTED_LIST:
                if (unwanted_product in product['title']):
                    logger.info(f"skip the product contain: {unwanted_product} in: {product['title']}")
                    skip_product = True
            if(skip_product == True):
                continue
            ###price
            product['price'] = product['price'].lower()
            #skipping(removing) sold item
            if ("venduto" in product['price']):
                logger.info(f"skip the product is already sold {product['price']}")
                continue
            #check 'shipping_available' boolean
            if ("spedizione disponibile" in product['price']):
                logger.info(f"Setting shipping_available to true")
                product['shipping_available'] = True
            try:
                #removing the $Spedizone disponibile, taking only the numeric part converted to int
                product['price'] = float(product['price'].split()[0])
                #removing low price for spam product accessory broken phone ecc
                if (product['price'] <= 150.00):
                    logger.info(f"{product['price']} is too low for {product['title']}")
                    continue
            except Exception as e:
                logger.error(f"Price conversion error: {e}")
                continue
            
            ###province
            #regex to remove both parenthesis
            product['province'] = re.sub(r"[()]", "", product['province'])
            ###city
            product['city'] = product['city'].lower()
            ###date
            product['date_scraped'] = datetime.now()

            collection.update_one(filter_query, update_statement, upsert=True)
            cleaned_data.append(product)

        ## returning a fresh list tha has not been modified by mongodb update_one or insert_many (does not containt objectId created by mongodb) avoid serialization errors 
        return {"message": "Scrape success and data saved.", "result" : cleaned_data}
    
    except Exception as e:
        logger.error(f"Error saving data to mongodb: {e}")
        return {f"message": "error saving data to mongodb", "error" : str(e)}