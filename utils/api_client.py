import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "x-api-key": "reqres-free-v1"
        }
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload)
        return response