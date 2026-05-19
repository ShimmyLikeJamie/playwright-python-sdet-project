import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_sort_functional(logged_in_page: Page):
    #0 Initialize inventory page object
    inventory = InventoryPage(logged_in_page)

    #1 Find the sort dropdown and select 'Price (low to high)'
    inventory.change_sort_order("lohi")

    #2 Verify the top item is the onesie 
    expect(inventory.first_item_name).to_have_text("Sauce Labs Onesie")

    #3 Verify that the products are sorted by price low to high
    prices = inventory.item_prices.all_inner_texts()
    # Convert price strings to floats
    prices = [float(price.replace("$", "")) for price in prices]
    assert prices == sorted(prices), "Items are not properly sorted!"