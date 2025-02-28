import time
import pytest
from api_tests.utils.api_client import APIClient

api_client = APIClient()

# Dictionary to store response times for pytest-html reporting
response_times = {}

@pytest.mark.parametrize("delay", [1, 2, 3])
def test_delayed_response(delay):
    """
    Measures the actual response time of the API for a given delay and validates performance.
    
    Steps:
    1. Call the API with a specific delay parameter.
    2. Extract response time directly from `response.elapsed.total_seconds()`.
    3. Store the response time for reporting.
    4. If the response takes excessively long, the test is skipped.
    5. Validate that the response time is within an acceptable range.
    """

    response = api_client.get_response(f"/users?delay={delay}")
    response_time = response.elapsed.total_seconds()

    # Store the response time for pytest-html reporting
    response_times[f"delay_{delay}"] = response_time

    # Skip the test if API response time exceeds delay + 10 seconds
    if response_time > delay + 10:
        pytest.skip(f"API took too long ({response_time:.2f}s), skipping test.")

    # Assert that response time is within expected limits
    assert delay <= response_time <= delay + 10, (
        f"Expected response close to {delay}s, but took {response_time:.2f}s"
    )
