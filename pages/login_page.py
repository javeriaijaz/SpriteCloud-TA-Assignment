from pages.base_page import BasePage
from locators.locators import LoginPageLocators  # Importing locators

class LoginPage(BasePage):
    """ Page Object Model for the Login Page of SauceDemo """

    # Base URL for the login page
    URL = "https://www.saucedemo.com"

    def open(self):
        """ Opens the login page in the browser """
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Performs login action by:
        1. Entering username
        2. Entering password
        3. Clicking the login button
        """
        self.enter_text(LoginPageLocators.USERNAME_INPUT, username)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        """ Retrieves the error message when login fails """
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)
