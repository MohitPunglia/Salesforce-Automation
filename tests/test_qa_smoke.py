# tests/test_qa_smoke.py
import pytest
import time
from pages.login_page import LoginPage
from config.base_config import config
from selenium.webdriver.common.by import By

class TestQASmoke:
    """Smoke test for QA environment"""
    
    @pytest.mark.qa
    def test_qa_url_loading(self, browser):
        """Test that QA Salesforce URL loads successfully"""
        print(f"\n🌐 Testing URL: {config.base_url}")
        
        # Load the login page
        login_page = LoginPage(browser)
        login_page.load(config.base_url)
        
        # Verify we reached a Salesforce page
        assert "salesforce" in browser.current_url.lower(), f"Not a Salesforce URL: {browser.current_url}"
        print("✅ Successfully loaded Salesforce page")
        
        # Check page title
        assert "login" in browser.title.lower(), f"Unexpected page title: {browser.title}"
        print("✅ Page title contains 'login'")
        
        # Take screenshot for verification
        browser.save_screenshot("qa_login_page.png")
        print("✅ Screenshot saved: qa_login_page.png")

    @pytest.mark.qa
    def test_login_form_elements(self, browser):
        """Test that login form elements are present and interactable"""
        login_page = LoginPage(browser)
        login_page.load(config.base_url)
        
        # Verify username field
        username_field = browser.find_element(By.ID, "username")
        assert username_field.is_displayed(), "Username field not visible"
        assert username_field.is_enabled(), "Username field not enabled"
        print("✅ Username field is ready")
        
        # Verify password field
        password_field = browser.find_element(By.ID, "password")
        assert password_field.is_displayed(), "Password field not visible"
        assert password_field.is_enabled(), "Password field not enabled"
        print("✅ Password field is ready")
        
        # Verify login button
        login_button = browser.find_element(By.ID, "Login")
        assert login_button.is_displayed(), "Login button not visible"
        assert login_button.is_enabled(), "Login button not enabled"
        print("✅ Login button is ready")

    @pytest.mark.qa
    def test_enter_credentials(self, browser):
        """Test that we can enter text into login fields"""
        login_page = LoginPage(browser)
        login_page.load(config.base_url)
        
        # Enter text into username field
        username_field = browser.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys("test_username@qa.com")
        entered_username = username_field.get_attribute("value")
        assert entered_username == "test_username@qa.com", f"Username not entered correctly: {entered_username}"
        print("✅ Username field accepts input")
        
        # Enter text into password field
        password_field = browser.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("test_password123")
        entered_password = password_field.get_attribute("value")
        assert entered_password == "test_password123", f"Password not entered correctly: {entered_password}"
        print("✅ Password field accepts input")
        
        # Don't actually click login to avoid failed attempts
        print("✅ Credential entry test completed - no actual login attempted")
