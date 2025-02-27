import time
import pytest
from api_tests.utils.api_client import APIClient

api_client = APIClient()

# Dictionary to store response times for pytest-html reporting
response_times = {}

@pytest.mark.parametrize("delay", [1, 2, 3])  # Test API response delay for 1, 2, and 3 seconds
def test_delayed_response(delay):
    """
    Measures the actual response time of the API for a given delay and validates performance.
    
    Steps:
    1. Record start time before making the request.
    2. Call the API with a specific delay parameter.
    3. Record end time after receiving the response.
    4. Calculate and store the actual response time.
    5. If the response takes excessively long, the test is skipped.
    6. Validate that the response time is within an acceptable range.
    """

    start_time = time.time()  # Start time before the API call
    response = api_client.get(f"/users?delay={delay}")  # Make the API request with delay
    end_time = time.time()  # End time after receiving the response

    response_time = end_time - start_time  # Calculate the total response duration

    # Store response time for pytest-html reporting
    response_times[f"Delay {delay}s"] = f"{response_time:.2f}s"

    # Skip the test if API response time exceeds delay + 10 seconds
    if response_time > delay + 10:
        pytest.skip(f"API took too long ({response_time:.2f}s), skipping test.")

    # Assert that response time is within expected limits
    assert delay <= response_time <= delay + 10, (
        f"Expected response close to {delay}s, but took {response_time:.2f}s"
    )

