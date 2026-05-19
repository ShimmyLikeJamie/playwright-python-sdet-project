from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch the browser (headless=False lets you see it happen)
        browser = p.chromium.launch(headless=False)
        
        # Create a new page
        page = browser.new_page()
        
        # Navigate to a website
        print("Navigating to example.com...")
        page.goto("https://example.com")
        
        # Get the page title
        title = page.title()
        
        # Log the success message
        print(f"Success! The page title is: '{title}'")
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    run()