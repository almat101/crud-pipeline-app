from fastapi import FastAPI
import requests
import logging
import datetime
from fastapi.middleware.cors import CORSMiddleware

# Configure logging to display messages at the INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger instance for this module


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost"],  # Same as your Express config
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def hello():
    return {"message":"hello from orchestrator-service!"}

@app.get("/orchestrate/{category}/")
def orchestrate(category: str, q: str):
    """
    Orchestrates the data pipeline by sequentially triggering the scraper-service and transformer-service.

    Path Parameters:
        category (str): The product category to search (passed as a path parameter).

    Query Parameters:
        q (str): The required query string representing the product name to search for.

    This endpoint first sends a GET request to the scraper-service to start the scraping process,
    passing both the category (path) and q (query string) parameters.
    If the scraping is successful (HTTP 2xx), it then sends a POST request to the transformer-service,
    passing the query string parameter q to start the data transformation and loading process.
    If either service fails, an error message indicating which service failed and the reason is returned.

    Returns:
        dict: A dictionary containing the JSON responses from both services if successful,
              or an error message specifying which service failed and the error details.
    """
    try:
        query = {'q' : q}
        scrape_response = requests.get(f"http://scraper-service:3040/scrape/{category}/", params=query, timeout=10)
        logger.info(scrape_response.url)
        scrape_response.raise_for_status()
        logger.info(f"scrape-service response: {scrape_response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request to scraper_service failed: {e}")
        return {"Error:" "scaper-service failed for":  str(e)}

    try:
        query = {'q': q}
        transform_response = requests.post("http://transformer-service:3050/transform", params=query, timeout=10)
        logger.info(transform_response.url)
        transform_response.raise_for_status()
        logger.info(f"transform-service response: {transform_response.text}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request to transform_service failed: {e}")
        return {"Error:" "tranform-service failed for":  str(e)}
    
    return {
        "status": "success",
        "message": "Pipeline orchestration completed successfully",
        "timestamp": datetime.datetime.now().isoformat(),
        "services": {
            "scraper": {
                "status": "success",
                "message": scrape_response.json().get("message", "Scraping completed")
            },
            "transformer": {
                "status": "success", 
                "message": transform_response.json().get("message", "Transformation completed")
            }
        }
    }