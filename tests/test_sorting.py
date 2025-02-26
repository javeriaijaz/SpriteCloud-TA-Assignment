# tests/test_sorting.py
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")  # Assuming the setup fixture is defined for browser setup
class TestSorting:
    """Test case for validating sorting functionality by name (Z-A)."""

    def test_sorting_by_name_Z_A(self, setup):
        """ 
        Test Case: Verify that sorting items by name Z-A works correctly.

        Steps:
        1. Login to the application.
        2. Navigate to the inventory page.
        3. Select 'Z-A' sorting from the dropdown.
        4. Retrieve and store the product names after sorting.
        5. Validate that the product names are sorted in reverse alphabetical order (Z-A).
        6. Ensure that the sorting is correct by validating against the sorted list.
        
        Expected Result:
        - The product names should be sorted in reverse (Z-A) order.
        """

        # Get the WebDriver instance to interact with the page
        driver = setup  
        login_page = LoginPage(driver)  # Initialize the login page
        inventory_page = InventoryPage(driver)  # Initialize the inventory page

        # Step 1: Log in to the application first
        login_page.open()  # Open the login page
        login_page.login("standard_user", "secret_sauce")  # Log in with standard user credentials

       # Step 2: Get the product names before sorting
        product_names_before_sorting = inventory_page.get_product_names()

        # Step 3: Apply Z-A sorting from the dropdown
        inventory_page.select_sort_order("Name (Z to A)")

        # Step 4: Get the product names after sorting
        product_names_after_sorting = inventory_page.get_product_names()

        # Step 5: Reverse the product names before sorting to simulate the expected Z-A order
        reversed_product_names_before_sorting = list(reversed(product_names_before_sorting))

        # Step 6: Assert that the product names after sorting match the reversed list from before sorting
        assert product_names_after_sorting == reversed_product_names_before_sorting, \
            f"Sorting failed! Expected reverse order, but got {product_names_after_sorting}"
