import requests
from config import Config
from http import HTTPStatus

class APIClient:
    """A generic API client for Reqres."""

    def __init__(self):
        self.base_url = Config.API_BASE_URL

    def get(self, endpoint, params=None):
        """Perform a GET request."""
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return self._validate_response(response)
    
    def get_response(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return response 

    def post(self, endpoint, data=None):
        """Perform a POST request."""
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        return self._validate_response(response)

    def put(self, endpoint, data=None):
        """Perform a PUT request."""
        response = requests.put(f"{self.base_url}{endpoint}", json=data)
        return self._validate_response(response)

    def delete(self, endpoint):
        """Perform a DELETE request."""
        response = requests.delete(f"{self.base_url}{endpoint}")
        return self._validate_response(response, allow_empty=True)

    def _validate_response(self, response, allow_empty=False):
        """Validate response status and return JSON or raise exception."""
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.NO_CONTENT] and (allow_empty or response.text):
            return response.json() if response.text else {}
        else:
            raise Exception(
                f"API Error: {response.status_code}, Response: {response.text}"
            )
