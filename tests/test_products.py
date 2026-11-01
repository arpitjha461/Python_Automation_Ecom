import logging

import requests

BASE_URL= "http://localhost:8765"
logger = logging.getLogger(__name__)


def test_get_all_products_without_token():
    logger.info("Starting GET all products test")
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    
    logger.info(f"Response : {response}")
    logger.info("API response status: %s", response.status_code)

    assert response.status_code ==403
    logger.info("GET products without token test passed")
    
    