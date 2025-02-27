from api_tests.utils.api_client import APIClient
from api_tests.utils.schemas import validate_json, USER_LIST_SCHEMA
from faker import Faker

fake = Faker()
api_client = APIClient()

api_client = APIClient()

def test_get_list_users():
    """Test retrieving a list of users."""
    response = api_client.get("/users?page=2")
    
    # Validate Status Code
    assert response["page"] == 2
    
    # Validate Schema
    validate_json(response, USER_LIST_SCHEMA)

def test_update_user():
    """Test updating a user's details."""
    payload = {"name": fake.first_name(), "job": "Senior QA Engineer"}
    response = api_client.put("/users/2", data=payload)
    
    # Validate Update
    assert response["job"] == "Senior QA Engineer"

def test_delete_user():
    """Test deleting a user."""
    response = api_client.delete("/users/2")
    
    # Validate Status Code
    assert response == {}  # Expect empty response