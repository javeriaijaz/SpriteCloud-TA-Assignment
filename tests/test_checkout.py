import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from faker import Faker

@pytest.mark.usefixtures("setup")
class TestCheckout:
    """Test case to validate the checkout process for at least two items"""

    def test_checkout_with_two_items(self, setup):
        """
        Test Case: Verify checkout process with two items and validate the final price.
        
        Steps:
        1. Log in to the application.
        2. Add at least two products to the cart.
        3. Navigate to the cart.
        4. Calculate the sum of the individual product prices.
        5. Complete the checkout Step One.
        6. Get item total from the checkout summary page and compare with sum of individual prices.
        7. Complete the checkout and verify the "Thank you" message.

        Expected Result:
        - The final item total on the checkout summary page matches the sum of the individual product prices, and the order is successfully placed with a "Thank you" message displayed.
        """

        driver = setup  # Use the driver from the setup fixture
        login_page = LoginPage(driver)  # Initialize the login page
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        fake = Faker()

        # Step 1: Log in
        login_page.open()  # Open the login page
        login_page.login("standard_user", "secret_sauce")  # Log in with standard user credentials

        # Step 2: Add two products to the cart
        product_page.add_product_to_cart("Sauce Labs Backpack")
        product_page.add_product_to_cart("Sauce Labs Bike Light")

        # Step 3: Go to the cart
        product_page.go_to_cart()

        # Step 4: Get item prices and validate total price
        item_prices = cart_page.get_item_prices()
        total_price_in_cart = sum(item_prices)

        # Step 5: Proceed to checkout
        cart_page.checkout()

        first_name, last_name, zip_code = fake.first_name(), fake.last_name(), fake.zipcode()
        checkout_page.enter_checkout_details(first_name, last_name, zip_code)
        checkout_page.click_continue()

        # Step 6: Get item total from checkout summary page
        displayed_total = checkout_page.get_displayed_item_total()
        assert displayed_total == total_price_in_cart, (
            f"Price mismatch! Expected: {total_price_in_cart}, but got: {displayed_total}"
        )

        # Step 7: Complete the checkout and Verify "Thank you" message
        checkout_page.click_finish()
        success_message = checkout_page.get_order_success_message()
        assert success_message == "Thank you for your order!", (
            f"Order completion failed! Expected: 'Thank you for your order!', but got: {success_message}"
        )
