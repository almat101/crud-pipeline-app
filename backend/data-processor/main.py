import logging
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCRAPE_URL= "https://www.subito.it/annunci-italia/vendita/elettronica/?q=thinkpad+t14"
SELECTOR_PRODUCTS = "div.SmallCard-module_upper-data-group__aRFDu"
SELECTOR_TITLE = "h2.headline-6.ItemTitle-module_item-title__VuKDo"
SELECTOR_CITY = "div.PostingTimeAndPlace-module_date-location__1Owcv span"
SELECTOR_PROVINCE = "div.PostingTimeAndPlace-module_date-location__1Owcv span.caption.small.city"
SELECTOR_PRICE = "p.index-module_price__N7M2x.x-SmallCard-module_price__yERv7.index-module_small__4SyUf"

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

        results = []
        for product in products:
            try:
                #Selenium is executing js to extract the title from css query selector using . to connect class name
                title = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_TITLE}')?.textContent || '';", product)
                city = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_CITY}')?.textContent || '';", product)
                province = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_PROVINCE}')?.textContent || '';", product)
                price = driver.execute_script(f"return arguments[0].querySelector('{SELECTOR_PRICE}')?.textContent || '';", product)
                # price_html = driver.execute_script("return arguments[0].outerHTML;", product)
                # logger.info(f"Price HTML: {price_html}")

                product_data = {
                    "title": title.strip(),
                    "city": city.strip(),
                    "province": province.strip(),
                    "price": price.strip(),
                }
                results.append(product_data)

            except Exception as e:
                # Log the error for this product and continue with the next one
                logger.error(f"Error scraping product: {e}")
                continue

        # Close the browser and clean up resources moved to finally block 
        #teardown(driver)

        # Log a message indicating the scraping process was completed successfully
        logger.info(f"Scraping completed succesfully: {results}")
        # Return a JSON response with a success message and the retrieved text
        return {"message": "Scrape success", "result": results}
    
    except Exception as e:
        logger.error(f"Error during scrape: {e}")
        return {"message": "scrape failed", "error" : str(e)}
    finally:
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