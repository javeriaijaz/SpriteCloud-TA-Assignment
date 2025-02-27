from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Locators for the Login Page"""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

class InventoryPageLocators:
    """Locators for the Inventory Page"""
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "div.inventory_item_name")

class CartPageLocators:
    """Locators for the Cart Page"""
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

class CheckoutPageLocators:
    """Locators for the Checkout Page"""
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.XPATH, "//button[text()='Finish']")
    ORDER_TOTAL = (By.CLASS_NAME, "summary_total_label")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Thank you for your order!')]")
