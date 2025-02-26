import pytest
from selenium import webdriver
import tempfile
import shutil

@pytest.fixture(scope="function")
def setup():
    # Create a unique temporary directory for each test's user data
    user_data_dir = tempfile.mkdtemp()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Unique user data directory for isolation
    chrome_options.add_argument("--disable-extensions")  # Disable extensions for test isolation
    chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues on CI environments
    chrome_options.add_argument("--remote-debugging-port=9222")  # Use a separate debugging port for isolation

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Yield the driver to the test

    driver.quit()  # Quit the WebDriver after the test

    # Clean up: Remove the temp directory after the test
    shutil.rmtree(user_data_dir)  # Delete the temp directory after each test
