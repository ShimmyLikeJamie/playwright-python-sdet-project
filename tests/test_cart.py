from playwright.sync_api import Page, expect

def test_cart(logged_in_page: Page):
    page = logged_in_page

    #1 Add backpack to cart using ID, which requires # symbol in front of it
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    #2 go to cart
    page.locator(".shopping_cart_link").click()

    #3 Verify backpack is in the cart
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()