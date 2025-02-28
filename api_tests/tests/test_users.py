from api_tests.utils.api_client import APIClient
from api_tests.utils.schemas import validate_json, USER_LIST_SCHEMA
from faker import Faker

fake = Faker()
api_client = APIClient()

PAGE_NUMBER = 2
USER_ID = 2
JOB_TITLE = "Senior QA Engineer"

def test_get_list_users():
    """Test retrieving a list of users."""
    
    response = api_client.get(f"/users?page={PAGE_NUMBER}")

    # Validate page value
    assert response["page"] == PAGE_NUMBER, f"Expected page {PAGE_NUMBER}, got {response['page']}"

    # Validate Schema
    validate_json(response, USER_LIST_SCHEMA)

def test_update_user():
    """Test updating a user's details."""
    
    payload = {"name": fake.first_name(), "job": JOB_TITLE}
    response = api_client.put(f"/users/{USER_ID}", data=payload)

    # Validate job update
    assert response["job"] == JOB_TITLE, f"Expected job '{JOB_TITLE}', got '{response['job']}'"

def test_delete_user():
    """Test deleting a user."""
    
    response = api_client.delete(f"/users/{USER_ID}")

    # Validate response is empty
    assert response == {}, f"Expected empty response, got {response}"
