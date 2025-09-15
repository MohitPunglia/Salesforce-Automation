
import allure
import pytest
import time
from pages.login_page import LoginPage
from config.base_config import config
from utils.screenshot_utils import capture_screenshot

class TestLogin:
    """ @pytest.mark.ui
    def test_login_page_loads(self, browser):  # ← Note: browser is passed as parameter
        "Test that the Salesforce login page loads successfully""
        login_page = LoginPage(browser)  # ← Pass browser to LoginPage
        #login_page.load("https://login.salesforce.com/")
        login_page.load(config.get_base_url())  # Use config
        
        # Verify page title contains "Login"
        assert "Login" in browser.title  # ← Use browser.title, not self.title
        print("Login page loaded successfully!")
    
    @pytest.mark.ui
    @pytest.mark.skip(reason="Requires valid Salesforce credentials")
    def test_valid_login(self, browser):  # ← browser parameter here too
        ""Test successful login (skipped by default)""
        login_page = LoginPage(browser)  # ← Pass browser to LoginPage
        login_page.load("https://login.salesforce.com/")
        
        # This will use the browser instance from the fixture
        login_page.login("your_username@example.com", "your_password")
        
        assert "lightning" in browser.current_url.lower() or "salesforce" in browser.current_url.lower()
        print("Login successful!") 
    
    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test successful login with valid credentials")
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_login(self, browser):
        with allure.step('Navigate to login page'): 
            print(f" Attempting login to: {config.base_url}")
            print(f"   Username: {config.get_username()}")
            
            # Initialize page object
            login_page = LoginPage(browser)
            
            # Navigate to login page using config URL
            login_page.load(config.base_url)
            print(" Login page loaded")
            allure.attach(
                browser.get_screenshot_as_png(),
                name="login_page_loaded",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Enter credentials"):        
            # Perform login with config credentials
            login_page.login(config.get_username(), config.get_password())
            print(" Login credentials submitted")
        
        with allure.step("Verify successful login"):
                # Wait for redirect (adjust time as needed)
                time.sleep(5)
                
                # Verify successful login by checking URL patterns
                current_url = browser.current_url.lower()
                print(f"   Current URL: {current_url}")
                
                # Check for successful login indicators
                success_indicators = [
                    "lightning", 
                    "salesforce",
                    "home", 
                    "one/one.app"  # Salesforce lightning experience
                ]
                
                # Verify we reached a post-login page
                assert any(indicator in current_url for indicator in success_indicators), \
                    f"Login failed! Expected post-login page, but got: {current_url}"   
                print(" Successful login completed!")
                print(f"   Redirected to: {browser.current_url}")    

                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="post_login_page",
                    attachment_type=allure.attachment_type.PNG
                )   """

    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_login(self, browser):
        try:
            login_page = LoginPage(browser)
            login_page.load(config.base_url)
            
            # Capture evidence
            capture_screenshot(browser, "login_page_loaded", "info")
            
            login_page.login(config.get_username(), config.get_password())
            time.sleep(5)
            
            # Verify login success
            current_url = browser.current_url.lower()
            assert any(indicator in current_url for indicator in ["lightning", "salesforce", "home"])
            
            # Capture success evidence
            capture_screenshot(browser, "login_successful", "passed")
            print(" Login successful!")
            
        except Exception as e:
            # Capture failure evidence
            capture_screenshot(browser, "login_failed", "failed")
            raise e

# Add this simple test to verify the fixture works
def test_browser_fixture_works(browser):
    """Simple test to verify the browser fixture works correctly"""
    browser.get(config.base_url)
    assert "Login" in browser.title
    assert "salesforce" in browser.current_url.lower()
    print("Browser fixture is working correctly!")