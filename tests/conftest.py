import pytest, logging, os
from playwright.sync_api import Page
#import LoginPage class defined in login_page.py
from pages.login_page import LoginPage

#The site uses data-test instead of data-testid, so we need to 
#tell pytest to look for that instead

def pytest_configure(config):
    #Create a logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Configure logging settings
    logging.basicConfig(
        level=logging.INFO, # Capture INFO, WARNING, ERROR logs
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("logs/test_run.log", mode="w"), # Save to a file (overwrites each run)
            logging.StreamHandler()                            # Print to terminal console
        ]
    )

@pytest.fixture(scope="session", autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def logged_in_page(page: Page):
    # This setup runs before every test that uses this fixture
    page.goto("https://www.saucedemo.com/")

    #initialize the LoginPage class with the page object
    login_page = LoginPage(page)
    #navigate to the page
    login_page.navigate()
    #login with credentials
    login_page.login("standard_user", "secret_sauce")
    
    # The 'yield' statement passes the page to the test
    yield page
    
    # (Optional) You could put cleanup code here, like logging out
    print("\nTest finished, cleaning up...")