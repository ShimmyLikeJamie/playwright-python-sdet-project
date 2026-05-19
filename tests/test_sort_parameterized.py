import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("sort_option, expected_first_item", [
    ("az", "Sauce Labs Backpack"),
    ("za", "Test.allTheThings() T-Shirt (Red)"),
    ("lohi", "Sauce Labs Onesie"),
    ("hilo", "Sauce Labs Fleece Jacket")
])
def test_sort_parameterized(logged_in_page: Page, sort_option, expected_first_item):
    inventory = InventoryPage(logged_in_page)

    #1 change sort order based on parameter
    inventory.change_sort_order(sort_option)

    #2 Verify the top item is correct based on the sort option
    expect(inventory.first_item_name).to_have_text(expected_first_item)