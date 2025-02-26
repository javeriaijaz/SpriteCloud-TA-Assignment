# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        """Initialize with WebDriver and set a default wait time."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        """Wait for element presence and return it."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element {locator} not found in {timeout} seconds.")

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible and return it."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=30):
        """Wait for element to be clickable and return it."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=30):
        """Wait for element to be clickable and perform a click."""
        self.wait_for_element_clickable(locator, timeout).click()

    def enter_text(self, locator, text, timeout=30):
        """Wait for input field, clear it, and enter text."""
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=30):
        """Wait for element to be visible and return its text."""
        return self.wait_for_element_visible(locator, timeout).text

    def is_element_present(self, locator, timeout=30):
        """Check if element is present within timeout."""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def get_elements_text(self, locator, timeout=10):
        """Retrieve text from multiple elements as a list."""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]