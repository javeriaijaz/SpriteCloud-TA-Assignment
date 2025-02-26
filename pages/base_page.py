# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default wait time of 10 seconds

    def find_element(self, locator, timeout=10):
        """Waits for an element to be present and returns it."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element with locator {locator} was not found within {timeout} seconds.")

    def wait_for_element_visible(self, locator, timeout=10):
        """Waits for an element to be visible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=30):
        """Waits for an element to be clickable before clicking."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=30):
        """Waits for the element to be clickable before clicking."""
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=30):
        """Waits for the input field to be visible before entering text."""
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()  # Clear any existing text before entering new text
        element.send_keys(text)

    def get_text(self, locator, timeout=30):
        """Waits for an element to be visible and returns its text."""
        return self.wait_for_element_visible(locator, timeout).text

    def is_element_present(self, locator, timeout=30):
        """Returns True if an element is present within the timeout, False otherwise."""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def get_elements_text(self, locator, timeout=10):
        """Retrieve text from multiple elements as a list."""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]