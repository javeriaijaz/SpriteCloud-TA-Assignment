import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    """Test cases for validating login functionality."""

    @pytest.mark.test_metadata(
        steps=[
            "Open the login page",
            "Attempt to log in with incorrect credentials",
            "Verify that an error message is displayed"
        ],
        expected="The error message should contain 'Epic sadface', indicating login failure."
    )
    @pytest.mark.parametrize("username, password", [("wrong_user", "wrong_pass")])
    def test_invalid_login(self, setup, username, password):
        """
        Test Case: Verify that an invalid login attempt shows the correct error message.
        """
        driver = setup  # Assign the WebDriver instance from the pytest fixture
        login_page = LoginPage(driver)  # Initialize the LoginPage with WebDriver

        login_page.open()  # Open the SauceDemo login page
        login_page.login(username, password)  # Enter invalid credentials

        # Validate that the correct error message is displayed
        assert "Epic sadface" in login_page.get_error_message(), "Error message is incorrect!"
