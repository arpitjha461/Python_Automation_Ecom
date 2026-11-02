
from utils.api_client import APIClient

client = APIClient("http://localhost:8765")



print(client.base_url)
print(client.timeout)
print(client.session)