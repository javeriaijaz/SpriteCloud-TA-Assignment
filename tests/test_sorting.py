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

        # Step 2: Now, let's change the sorting order to Z-A
        inventory_page.select_sort_order("Name (Z to A)")  # This selects the 'Z-A' sorting from the dropdown

        # Step 3: Get the product names after sorting
        product_names_after_sorting = inventory_page.get_product_names()

        # Step 4: Check if the product names are correctly sorted in reverse (Z-A) order
        sorted_product_names = sorted(product_names_after_sorting, reverse=True)

        # Let's assert that the products are indeed sorted Z-A
        assert product_names_after_sorting == sorted_product_names, f"Sorting failed! Expected Z-A order, but got {product_names_after_sorting}"

