# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")  # Locator for the sorting dropdown
    PRODUCTS_LIST = (By.CSS_SELECTOR, "div.inventory_item_name")  # Locator for the product names
    
    def select_sort_order(self, order="Z-A"):
        """Select sorting order from the dropdown."""
        self.find_element(self.SORT_DROPDOWN).click()
        sort_option = (By.XPATH, f"//option[text()='{order}']")
        self.find_element(sort_option).click()
        
    def get_product_names(self):
        """Get the names of all products displayed."""
        return self.get_elements_text(self.PRODUCTS_LIST)
