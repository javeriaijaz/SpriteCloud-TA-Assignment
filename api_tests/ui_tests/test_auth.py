import pytest
from api_tests.utils.api_client import APIClient

api_client = APIClient()

def test_successful_login():
    """Test successful login with valid credentials."""
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = api_client.post("/login", data=payload)
    
    # Validate Status Code & Token
    assert "token" in response
