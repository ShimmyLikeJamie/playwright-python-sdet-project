from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.get_by_test_id("product-sort-container")
        self.cart_icon = page.get_by_test_id("shopping-cart-link")
        self.item_prices = page.get_by_test_id("inventory-item-price")
        self.first_item_name = page.locator(".inventory_item_name").first

    def change_sort_order(self, sort_option: str):
        #Should be one of "az", "za", "lohi", "hilo"
        self.sort_dropdown.select_option(sort_option)

    def add_item_to_cart(self, item_id: str):
        self.page.get_by_test_id(item_id).click()

    def go_to_cart(self):
        self.cart_icon.click()