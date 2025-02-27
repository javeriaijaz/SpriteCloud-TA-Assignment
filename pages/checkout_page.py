from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    """Checkout Page - Handles actions related to completing the checkout process"""

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ORDER_TOTAL = (By.CLASS_NAME, "summary_total_label")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def enter_checkout_details(self, first_name, last_name, zip_code):
        """Fill in the checkout form with customer details"""
        self.enter_text(self.FIRST_NAME_FIELD, first_name) 
        self.enter_text(self.LAST_NAME_FIELD, last_name) 
        self.enter_text(self.ZIP_CODE_FIELD, zip_code)  

    def click_continue(self):
        """Click the Continue button to proceed"""
        self.click(self.CONTINUE_BUTTON) 

    def get_order_total(self):
        """Returns the order total after checkout"""
        total_text = self.get_text(self.ORDER_TOTAL) 
        return float(total_text.split('$')[1].strip())

    def get_displayed_item_total(self):
        """Returns the item total displayed on the checkout step two page."""
        total_text = self.get_text(self.ITEM_TOTAL) 
        return float(total_text.split("$")[1])

    def click_finish(self):
        """Clicks the 'Finish' button to complete the order"""
        self.click(self.FINISH_BUTTON)  

    def get_order_success_message(self):
        """Returns the order completion message"""
        return self.get_text(self.SUCCESS_MESSAGE) 
