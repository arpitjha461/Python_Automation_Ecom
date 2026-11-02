import logging
from utils.api_client import APIClient
import requests

BASE_URL= "http://localhost:8765"
logger = logging.getLogger(__name__)
client = APIClient(BASE_URL)


def test_get_all_products_without_token():
    logger.info("Starting GET all products test")
    response = client.get("/products")
    response1 = requests.get(f"{BASE_URL}/products", timeout=10)
    
    logger.info(f"Response1 : {response1}")
    logger.info(f"Response : {response}")
    logger.info("API response status: %s", response.status_code)

    assert response.status_code ==403
    logger.info("GET products without token test passed")
    
    