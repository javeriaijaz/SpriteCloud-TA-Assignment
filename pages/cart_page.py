from pages.base_page import BasePage
from pages.locators import CartPageLocators  # Importing locators

class CartPage(BasePage):
    """Cart Page - Handles actions related to viewing the cart and proceeding to checkout"""

    def get_item_prices(self):
        """Returns the prices of all items in the cart"""
        return [float(price.text[1:]) for price in self.driver.find_elements(*CartPageLocators.ITEM_PRICE)]

    def checkout(self):
        """Proceed to the checkout page"""
        self.click(CartPageLocators.CHECKOUT_BUTTON)
