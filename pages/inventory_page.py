# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import InventoryPageLocators  # Importing locators

class InventoryPage(BasePage):
    """ Page Object Model for the Inventory Page of SauceDemo """

    def select_sort_order(self, order="Z-A"):
        """Select sorting order from the dropdown."""
        self.find_element(InventoryPageLocators.SORT_DROPDOWN).click()
        sort_option = (By.XPATH, f"//option[text()='{order}']")
        self.find_element(sort_option).click()
        
    def get_product_names(self):
        """Get the names of all products displayed."""
        return self.get_elements_text(InventoryPageLocators.PRODUCTS_LIST)

