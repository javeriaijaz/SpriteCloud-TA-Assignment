import pytest
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
        response = str(e)  # Convert exception message to string for assertion

    assert "API Error: 400" in response  # Ensure correct status code
    assert "user not found" in response  # Ensure correct error message


def test_login_with_missing_password():
    """Negative test: Login without providing a password should return an error."""
    payload = {"email": Config.TEST_USER_EMAIL}  # Missing password

    try:
        response = api_client.post("/login", data=payload)
    except Exception as e:
        response = str(e)  # Convert exception message to string for assertion

    assert "API Error: 400" in response  # Ensure correct status code
    assert "Missing password" in response  # Ensure correct error message

def test_get_non_existing_user():
    """Negative test: Fetching a non-existing user should return 404."""
    try:
        response = api_client.get("/users/99999")  # Request for a non-existent user
    except Exception as e:
        print("Exception:", e)  # Debugging
        assert "404" in str(e), f"Expected 404 error but got {str(e)}"
