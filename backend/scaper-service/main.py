import logging
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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


# SCRAPE_URL="https://www.subito.it/annunci-italia/vendita/elettronica/?q=thinkpad+t14"
# PRODUCT_NAME="thinkpad t14"
SCRAPE_URL="https://www.subito.it/annunci-italia/vendita/elettronica/?q=iphone+15"

SELECTOR_PRODUCTS = "a.SmallCard-module_link__hOkzY"
# SELECTOR_PRODUCTS = "div.SmallCard-module_upper-data-group__aRFDu"
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
    """
    Scrapes product data from the target website using Selenium, processes and cleans the extracted data,
    and saves the results into MongoDB. Handles filtering, normalization, and error logging.

    Returns:
        dict: A response message and the list of cleaned products if successful,
              or an error message if scraping or saving fails.
    """
    driver = None
    try:
        logger.info("selenium driver start..")
        # Initialize the Selenium WebDriver
        driver = setup()

        # Get the title of the current webpage
        title = driver.title

        # Set an implicit wait time of 5 seconds for finding elements
        driver.implicitly_wait(5)

        print(driver.page_source)

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

                product_data = {
                    "title": title,
                    "city": city,
                    "province": province,
                    "price": price,
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
    """
    Initializes the Selenium WebDriver (Chrome) and navigates to the target URL.

    Returns:
        webdriver.Chrome: The initialized WebDriver instance.

    Raises:
        Exception: If there is an error during WebDriver setup.
    """
    try:

        options = get_custom_chrome_options()
        # Inizializing the webdriver with custom options
        driver = webdriver.Chrome(options=options)
        driver.get(SCRAPE_URL)
        return driver  # Return the WebDriver instance
    except Exception as e:
        logger.error(f"Error on setup webdriver: {e}")
        raise # Re-raises the same exception


def teardown(driver):
    """
    Quits the Selenium WebDriver and closes the browser.

    Args:
        driver (webdriver.Chrome): The WebDriver instance to quit.

    Logs:
        Any exception that occurs during the teardown process.
    """
    try:
        # Quit the WebDriver and close the browser
        driver.quit()
    except Exception as e:
        logger.error(f"Error during WebDriver teardown: {e}")

def saving_data(raw_data):
    """
    Adds the current datetime to each product in the raw data and saves them to MongoDB.
    Data is stored as scraped, with only the date_scraped field added.
    No filtering or cleaning on the products, we are saving raw data as scraped(immutability of data)
    Filtering and cleaning will be done in another microservice(separation of concern)

    Args:
        raw_data (list): List of dictionaries containing the raw product data.

    Returns:
        dict: Success message and the list of products saved to MongoDB,
              or an error message if saving fails.
    """
    try:
        data = []
        ### delete all elements in the collections
        # collection.delete_many({})
        for product in raw_data:
            filter_query = {"title": product["title"]}  # This finds a document with the same title
            update_statement = {"$set": product}       # This sets all fields to the new data
            ###title
            # product['title'] = product['title']
            ###price
            # product['price'] = product['price']

            # product['province'] = product['province']
            ###city
            # product['city'] = product['city']
            ###date
            product['date_scraped'] = datetime.now()

            collection.update_one(filter_query, update_statement, upsert=True)
            data.append(product)

        ## returning a fresh list tha has not been modified by mongodb update_one or insert_many (does not containt objectId created by mongodb) avoid serialization errors 
        return {"message": "Scrape success and data saved to mongodb.", "result" : data}
    
    except Exception as e:
        logger.error(f"Error saving data to mongodb: {e}")
        return {f"message": "error saving data to mongodb", "error" : str(e)}
    

def get_custom_chrome_options():
    """
        Creates and configures a ChromeOptions object for Selenium WebDriver to reduce bot dedection.

        The options are set to:
        - Enable headless mode (not opening a browser window).
        - Specify a standard desktop window size to mimic a real user and avoid mobile layouts.
        - Use a real browser user-agent to reduce bot detection.

        Additional options for Docker or CI environments are included as comments for future use if needed:
        - --no-sandbox: Disables Chrome security sandbox. Needed in Docker/CI environments where the sandbox can cause permission errors.
        - --disable-dev-shm-usage: Tells Chrome not to use /dev/shm (shared memory). In Docker, the default shared memory size can be too small, causing Chrome to crash.
        - --disable-blink-features=AutomationControlled: Tries to hide the fact that you’re using Selenium. Some sites check for this feature to block bots.

        Returns:
            webdriver.ChromeOptions: A configured ChromeOptions object for use with Selenium.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    ### This options may be needed when running in a docker environment ###
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("window-size=1920,1080")
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    return options