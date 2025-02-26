import pytest
from selenium import webdriver
import tempfile
import shutil

@pytest.fixture(scope="function")
def setup():
    # Create a temporary directory for user data (unique for each test)
    user_data_dir = tempfile.mkdtemp()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Unique user data directory

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Yield the driver to the test

    driver.quit()  # Quit the WebDriver after the test

    # Clean up: Remove the temp directory after the test
    shutil.rmtree(user_data_dir)
