import pytest
from playwright.sync_api import Page, expect

def test_basic_navigation(page: Page):
    #1 nav to practice site
    page.goto("https://www.saucedemo.com/")

    #2 Check if logo or title is correct
    #'expect' waits automatically for the element to appear
    expect(page).to_have_title("Swag Labs")

    print("Nav success!")

def test_failed_login_message(page: Page):
    page.goto("https://saucedemo.com/")

    #try to find username field and type 'wrong_user'
    #then find password field and type 'wrong_password'
    #then click login button

    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    #expect error message to be visible
    expect(page.get_by_text("Username and password do not match")).to_be_visible()
    expect(page).to_have_url("https://www.saucedemo.com/") #should still be on login page