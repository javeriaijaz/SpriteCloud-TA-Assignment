from pages.base_page import BasePage
from locators.locators import CheckoutPageLocators  # Importing locators

class CheckoutPage(BasePage):
    """Checkout Page - Handles actions related to completing the checkout process"""

    def enter_checkout_details(self, first_name, last_name, zip_code):
        """Fill in the checkout form with customer details"""
        self.enter_text(CheckoutPageLocators.FIRST_NAME_FIELD, first_name)
        self.enter_text(CheckoutPageLocators.LAST_NAME_FIELD, last_name)
        self.enter_text(CheckoutPageLocators.ZIP_CODE_FIELD, zip_code)

    def click_continue(self):
        """Click the Continue button to proceed"""
        self.click(CheckoutPageLocators.CONTINUE_BUTTON)

    def get_order_total(self):
        """Returns the order total after checkout"""
        total_text = self.get_text(CheckoutPageLocators.ORDER_TOTAL)
        return float(total_text.split('$')[1].strip())

    def get_displayed_item_total(self):
        """Returns the item total displayed on the checkout step two page."""
        total_text = self.get_text(CheckoutPageLocators.ITEM_TOTAL) 
        return float(total_text.split("$")[1])

    def click_finish(self):
        """Clicks the 'Finish' button to complete the order"""
        self.click(CheckoutPageLocators.FINISH_BUTTON)

    def get_order_success_message(self):
        """Returns the order completion message"""
        return self.get_text(CheckoutPageLocators.SUCCESS_MESSAGE)
