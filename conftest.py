import pytest
from selenium import webdriver
import tempfile
import os

@pytest.fixture(scope="function")
def setup():
    # Create a temporary directory for user data
    user_data_dir = tempfile.mkdtemp()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Unique user data directory

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # This will provide the WebDriver instance to the tests

    # Clean up after the test (e.g., delete temporary user data directory)
    driver.quit()
    try:
        os.rmdir(user_data_dir)  # Remove the temp user data directory after the test
    except Exception as e:
        print(f"Failed to remove temp directory: {e}")
