import pytest
from selenium import webdriver
import tempfile
import shutil
import psutil
import os
import signal

@pytest.fixture(scope="function")
def setup():
    # Create a unique temporary directory for each test's user data
    user_data_dir = tempfile.mkdtemp()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Unique user data directory
    chrome_options.add_argument("--disable-extensions")  # Disable extensions for test isolation
    chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues on CI environments
    chrome_options.add_argument("--remote-debugging-port=9222")  # Use a separate debugging port for isolation

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Yield the driver to the test

    driver.quit()  # Quit the WebDriver after the test

    # Clean up: Remove the temp directory after the test
    shutil.rmtree(user_data_dir)

    # Ensure no lingering Chrome processes are left behind (this can happen on CI servers)
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chrome' in proc.info['name'].lower():
            os.kill(proc.info['pid'], signal.SIGTERM)
