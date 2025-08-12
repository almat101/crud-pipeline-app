import logging
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    # Locate the text input field by its ID and store it in a variable
    text_box = driver.find_element(by=By.ID, value="my-text-id")
    # Locate the submit button using a CSS selector
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # Enter the text "Selenium" into the text input field
    text_box.send_keys("Selenium")
    # Click the submit button to submit the form
    submit_button.click()
    
    # Locate the element with the ID "message" and retrieve its text content
    message = driver.find_element(by=By.ID, value="message")
    text = message.text  # Extract the text from the located element

    # Close the browser and clean up resources
    teardown(driver)

    # Log a message indicating the scraping process was completed successfully
    logger.info("Scraping completed succesfully")
    # Return a JSON response with a success message and the retrieved text
    return {"message": "Scrape success", "result": text}


def setup():
    # Initialize the Selenium WebDriver (Chrome) and navigate to the target URL
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver  # Return the WebDriver instance


def teardown(driver):
    # Quit the WebDriver and close the browser
    driver.quit()