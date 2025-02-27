from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """ Page Object Model for the Login Page of SauceDemo """
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        super().__init__(driver)
        
    def login(self, username, password):
        """
        Performs login action by:
        1. Entering username
        2. Entering password
        3. Clicking the login button
        """
        self.enter_text(self.USERNAME_INPUT, username) 
        self.enter_text(self.PASSWORD_INPUT, password) 
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """ Retrieves the error message when login fails """
        return self.get_text(self.ERROR_MESSAGE)  
