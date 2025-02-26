# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Uses Chrome WebDriver
    driver.maximize_window()
    yield driver
    driver.quit()



