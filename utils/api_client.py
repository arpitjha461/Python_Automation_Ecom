import requests
import logging

logger = logging.getLogger(__name__)

class APIClient:
    
    def __init__(self,base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session =requests.Session()
        
        
    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"  
        logger.info("Sending GET request: %s", url)
        
        response = self.session.get(url, timeout=self.timeout,**kwargs)        
        logger.info("GET request completed | Status: %s",response.status_code)
        
        return response
    
    
    