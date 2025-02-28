from api_tests.utils.api_client import APIClient
from config import Config
from faker import Faker

fake = Faker()

api_client = APIClient()

def test_login_with_invalid_email():
    """Negative test: Login with an incorrect email should return an error."""
    payload = {"email": fake.email(), "password": Config.TEST_USER_PASSWORD}

    try:
        response = api_client.post("/login", data=payload)
    except Exception as e:
        response = str(e)  

    assert "API Error: 400" in response
    assert "user not found" in response 


def test_login_with_missing_password():
    """Negative test: Login without providing a password should return an error."""
    payload = {"email": Config.TEST_USER_EMAIL}

    try:
        response = api_client.post("/login", data=payload)
    except Exception as e:
        response = str(e) 

    assert "API Error: 400" in response
    assert "Missing password" in response

def test_get_non_existing_user():
    """Negative test: Fetching a non-existing user should return 404."""
    try:
        response = api_client.get("/users/99999")
    except Exception as e:
        assert "404" in str(e), f"Expected 404 error but got {str(e)}"
