import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

@pytest.fixture(scope="module")
def browser():
    """Setup Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    
    # Only add headless mode and other CI-specific options when running in GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless")  # Headless only in CI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    else:
        # Options for local development with visible browser
        options.add_argument("--start-maximized")  # Start with maximized window
        options.add_argument("--disable-infobars")  # Disable info bars
        options.add_argument("--disable-extensions")  # Disable extensions
        
    # If running in GitHub Actions, use display
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--display=:99")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()  # Cleanup after test

def test_google_title(browser):
    """Test if Google homepage loads correctly"""
    try:
        browser.get("https://www.google.com")
        print(f"Current page title: {browser.title}")  # Debug info
        assert "Google" in browser.title, "Google title does not match!"
    except Exception as e:
        print(f"Error during test: {str(e)}")
        raise
