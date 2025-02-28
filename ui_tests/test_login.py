import pytest
from pages.login_page import LoginPage
from faker import Faker

fake = Faker()

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
    @pytest.mark.parametrize("username, password", [(fake.user_name(), fake.password())])
    def test_invalid_login(self, setup, username, password):
        """
        Test Case: Verify that an invalid login attempt shows the correct error message.
        """
        driver = setup
        login_page = LoginPage(driver)
        
        # Open the Login Page URL
        login_page.navigate_to_url()
        login_page.login(username, password)

        # Validate that the correct error message is displayed
        assert "Epic sadface" in login_page.get_error_message(), "Error message is incorrect!"
