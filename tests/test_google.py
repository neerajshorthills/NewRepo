import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

@pytest.fixture(scope="module")
def browser():
    """Setup Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    
    # Add necessary arguments for CI environment
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Required for running in container
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--window-size=1920,1080")  # Set window size
    
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
