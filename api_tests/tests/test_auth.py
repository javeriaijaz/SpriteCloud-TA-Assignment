from api_tests.utils.api_client import APIClient
from config import Config


api_client = APIClient()

def test_successful_login():
    """Test successful login with valid credentials."""
    payload = {"email": Config.TEST_USER_EMAIL, "password": Config.TEST_USER_PASSWORD}
    response = api_client.post("/login", data=payload)
    
    # Validate Token
    assert "token" in response
