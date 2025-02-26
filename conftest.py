import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

@pytest.fixture(scope="function")
def setup():
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")  # Disable extensions to ensure clean test runs
    chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues, common in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid issues related to limited memory in CI environments
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
    chrome_options.add_argument("--remote-debugging-port=9222")  # Use remote debugging port (for troubleshooting)
    chrome_options.add_argument("--verbose")  # Enable verbose logging

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver  # Yield the driver to the test

    driver.quit()  # Quit the WebDriver after the test is done
