import pytest
import chromedriver_autoinstaller
from selenium import webdriver

# Automatically install the appropriate ChromeDriver version that matches the installed version of Chrome
chromedriver_autoinstaller.install()

@pytest.fixture(scope="function")
def setup():
    # Set up Chrome options without user data dir and debugging port
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")  # Disable extensions to ensure test isolation
    chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues, common in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid memory issues in CI environments

    # Initialize the WebDriver with the above options
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Yield the driver to the test

    driver.quit()  # Quit the WebDriver after the test is complete
