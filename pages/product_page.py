from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.locators import ProductPageLocators  # Importing locators

class ProductPage(BasePage):
    """Product Page - Handles actions related to adding products to the cart"""

    def add_product_to_cart(self, product_name):
        """Add a product to the cart by clicking the Add to Cart button next to the product"""
        product_button = (By.ID, f"add-to-cart-{product_name.lower().replace(' ', '-')}") 
        self.click(product_button)

    def go_to_cart(self):
        """Navigate to the cart page to review items in the cart"""
        self.click(ProductPageLocators.CART_ICON)
