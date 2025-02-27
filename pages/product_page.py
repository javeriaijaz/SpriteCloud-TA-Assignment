from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Product Page - Handles actions related to adding products to the cart"""

    # Locators
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')

    def add_product_to_cart(self, product_name):
        """Add a product to the cart by clicking the Add to Cart button next to the product"""
        product_button = (By.ID, f"add-to-cart-{product_name.lower().replace(' ', '-')}") 
        self.click(product_button)

    def go_to_cart(self):
        """Navigate to the cart page to review items in the cart"""
        self.click(self.CART_ICON)
