import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    """Setup Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Opens in full screen
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()  # Cleanup after test

def test_google_title(browser):
    """Test if Google homepage loads correctly"""
    browser.get("https://www.google.com")
    assert "Google" in browser.title, "Google title does not match!"
