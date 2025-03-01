from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, StaleElementReferenceException
from config import Config
import time

class BasePage:

    URL = Config.BASE_URL

    def __init__(self, driver):
        """Initialize with WebDriver and set a default wait time."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def navigate_to_url(self):
        try:
            self.driver.get(self.URL)
        except Exception as e:
            raise Exception(f"Failed to navigate to URL: {self.URL}. Error: {str(e)}")

    def find_element(self, locator, timeout=30):
        """Wait for element presence and return it. Catch all exceptions."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Error finding element {locator}: {str(e)}")

    def wait_for_element_visible(self, locator, timeout=30):
        """Wait for element to be visible and return it. Catch all exceptions."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Error waiting for element {locator} to be visible: {str(e)}")

    def wait_for_element_clickable(self, locator, timeout=30):
        """Wait for element to be clickable and return it. Catch all exceptions."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            raise Exception(f"Error waiting for element {locator} to be clickable: {str(e)}")

    def click(self, locator, timeout=30):
        """Wait for element to be clickable and perform a click. Catch all exceptions and retry if needed."""
        for attempt in range(3):  # Retry up to 3 times
            try:
                element = self.wait_for_element_clickable(locator, timeout)
                element.click()
                return
            except Exception as e:
                print(f"Retrying click on {locator} (Attempt {attempt + 1}): {str(e)}")
                time.sleep(1)
        raise Exception(f"Failed to click element {locator} after multiple retries.")

    def enter_text(self, locator, text, timeout=30):
        """Wait for input field, clear it, and enter text. Catch all exceptions."""
        try:
            element = self.wait_for_element_visible(locator, timeout)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Error entering text in {locator}: {str(e)}")

    def get_text(self, locator, timeout=30):
        """Wait for element to be visible and return its text. Catch all exceptions."""
        try:
            return self.wait_for_element_visible(locator, timeout).text
        except Exception as e:
            raise Exception(f"Error getting text from element {locator}: {str(e)}")

    def is_element_present(self, locator, timeout=30):
        """Check if element is present within timeout. Catch all exceptions."""
        try:
            self.find_element(locator, timeout)
            return True
        except Exception as e:
            print(f"Element {locator} not found: {str(e)}")
            return False

    def get_elements_text(self, locator, timeout=30):
        """Retrieve text from multiple elements as a list. Catch all exceptions."""
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return [element.text for element in elements]
        except Exception as e:
            raise Exception(f"Error getting text from multiple elements {locator}: {str(e)}")
