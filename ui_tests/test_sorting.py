import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from config import Config

@pytest.mark.usefixtures("setup")
class TestSorting:
    """Test case for validating sorting functionality by name (Z-A)."""

    @pytest.mark.test_metadata(
        steps=[
            "Log in to the application",
            "Navigate to the inventory page",
            "Retrieve and store product names before sorting",
            "Apply 'Z-A' sorting from the dropdown",
            "Retrieve and store product names after sorting",
            "Reverse the product names from the initial list",
            "Compare the sorted list with the reversed list to ensure correct sorting"
        ],
        expected="Product names should be sorted in reverse alphabetical order (Z-A)."
    )
    def test_sorting_by_name_Z_A(self, setup):
        """ 
        Test Case: Verify that sorting items by name Z-A works correctly.
        """

        # Get login credentials from env file
        username = Config.USERNAME
        password = Config.PASSWORD

        # Get the WebDriver instance to interact with the page
        driver = setup  
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        # Step 1: Log in to the application
        # Step 2: Navigate to the inventory page 
        login_page.navigate_to_url()
        login_page.login(username, password)

        
        # Step 3: Retrieve and store product names before sorting
        product_names_before_sorting = inventory_page.get_product_names()

        # Step 4: Apply Z-A sorting from the dropdown
        inventory_page.select_sort_order("Name (Z to A)")

        # Step 5: Retrieve and store product names after sorting
        product_names_after_sorting = inventory_page.get_product_names()

        # Step 6: Reverse the product names before sorting to simulate the expected Z-A order
        reversed_product_names_before_sorting = list(reversed(product_names_before_sorting))
        assert product_names_after_sorting == reversed_product_names_before_sorting, \
            f"Sorting failed! Expected reverse order, but got {product_names_after_sorting}"
