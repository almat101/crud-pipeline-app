import logging
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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
    logger.info("selenium driver start..")
    # Initialize the Selenium WebDriver and navigate to the target URL
    driver = setup()

    # Get the title of the current webpage
    title = driver.title

    # Set an implicit wait time of 5 seconds for finding elements
    driver.implicitly_wait(5)

    # find all elements matching the css selector (changed to take the DIV father element)
    products = driver.find_elements(By.CSS_SELECTOR, "div.SmallCard-module_upper-data-group__aRFDu")

    # products = driver.find_elements(By.CSS_SELECTOR, "h2.headline-6.ItemTitle-module_item-title__VuKDo")

    # city = driver.find_elements(By.CSS_SELECTOR, )
    ##first try returns empty elements
    # results = [element.text for element in elements]

    ##second try works because is simulating user scroll down on the page like a real user
    # results = []
    # for element in elements:
    #     # Scroll to the element
    #     ActionChains(driver).move_to_element(element).perform()
    #     # Extract the text
    #     if element.text.strip():  # Ensure the text is not empty
    #         results.append(element.text)

    ##third try wotks but is using javascript to extract elements ( faster DOM manipulation, doesn't mimic real user)
    results = []
    for product in products:
        #Selenium is executing js to extract the title from css query selector using . to connect class name
        title = driver.execute_script("return arguments[0].querySelector('h2.headline-6.ItemTitle-module_item-title__VuKDo')?.textContent || '';", product)
        city = driver.execute_script("return arguments[0].querySelector('div.PostingTimeAndPlace-module_date-location__1Owcv span')?.textContent || '';", product)
        province = driver.execute_script("return arguments[0].querySelector('div.PostingTimeAndPlace-module_date-location__1Owcv span.caption.small.city')?.textContent || '';", product)
        price = driver.execute_script("return arguments[0].querySelector('p.index-module_price__N7M2x.x-SmallCard-module_price__yERv7 index-module_small__4SyUf')?.textContent || '';", product)
        # price_html = driver.execute_script("return arguments[0].outerHTML;", product)
        # logger.info(f"Price HTML: {price_html}")

        product_data = {
            "title": title.strip(),
            "city": city.strip(),
            "province": province.strip(),
            "price": price.strip(),
        }
        
        results.append(product_data)

    # text_box = driver.find_element(by=By.ID, value="my-text-id")
    # Locate the submit button using a CSS selector
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # # Enter the text "Selenium" into the text input field
    # text_box.send_keys("Selenium")
    # # Click the submit button to submit the form
    # submit_button.click()
    
    # # Locate the element with the ID "message" and retrieve its text content
    # message = driver.find_element(by=By.ID, value="message")
    # text = message.text  # Extract the text from the located element

    # Close the browser and clean up resources
    teardown(driver)

    # Log a message indicating the scraping process was completed successfully
    logger.info(f"Scraping completed succesfully: {results}")
    # Return a JSON response with a success message and the retrieved text
    return {"message": "Scrape success", "result": results}


def setup():
    # Initialize the Selenium WebDriver (Chrome) and navigate to the target URL
    driver = webdriver.Chrome()
    driver.get("https://www.subito.it/annunci-italia/vendita/elettronica/?q=thinkpad+t14")
    return driver  # Return the WebDriver instance


def teardown(driver):
    # Quit the WebDriver and close the browser
    driver.quit()