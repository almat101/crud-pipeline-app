from fastapi import FastAPI
import requests
import logging

# Configure logging to display messages at the INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger instance for this module


app = FastAPI()

@app.get("/")
def hello():
    return {"message":"hello from orchestrator-service!"}

@app.post("/orchestrate")
def orchestrate():
    """
    Orchestrates the data pipeline by sequentially triggering the scraper-service and transformer-service.

    This endpoint first sends a GET request to the scraper-service to start the scraping process.
    If the scraping is successful (HTTP 2xx), it then sends a POST request to the transformer-service
    to start the data transformation and loading process. If either service fails, an error message
    indicating which service failed and the reason is returned.

    Returns:
        dict: A dictionary containing the JSON responses from both services if successful,
              or an error message specifying which service failed and the error details.
    """
    try:
        scrape_response = requests.get("http://scraper-service:3040/scrape", timeout=10)
        scrape_response.raise_for_status()
        logger.info(f"scrape-service response: {scrape_response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request to scraper_service failed: {e}")
        return {"Error:" "scaper-service failed for":  str(e)}

    try:
        transform_response = requests.post("http://transformer-service:3050/transform", timeout=10)
        transform_response.raise_for_status()
        logger.info(f"transform-service response: {transform_response.text}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request to transform_service failed: {e}")
        return {"Error:" "tranform-service failed for":  str(e)}
    
    return {
        "scraper-service respnse" : scrape_response.json(),
        "transformer-service response" : transform_response.json()
    }