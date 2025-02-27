from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    """Cart Page - Handles actions related to viewing the cart and proceeding to checkout"""

    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_item_prices(self):
        """Returns the prices of all items in the cart"""
        return [float(price.text[1:]) for price in self.driver.find_elements(*self.ITEM_PRICE)] 

    def checkout(self):
        """Proceed to the checkout page"""
        self.click(self.CHECKOUT_BUTTON) 
