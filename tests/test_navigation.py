# tests/test_navigation.py
import pytest
import time
from pages.navigation_page import NavigationPage
from pages.login_page import LoginPage

class TestNavigation:
    def test_navigate_to_accounts_via_menu(self, browser):
        """Test complete flow: Open menu -> Select Accounts"""
        try:
            print("=" * 60)
            print("🚀 TEST: Navigate to Accounts via Navigation Menu")
            print("=" * 60)
            
            # Login first
            login_page = LoginPage(browser)
            login_page.navigate_to_login()
            
            # Login with credentials (replace with your actual credentials)
            login_success = login_page.login("your_username", "your_password")
            assert login_success, "Login failed"
            print("✅ Login successful")
            
            # Wait for page to load after login
            time.sleep(5)
            print(f"📄 Current URL: {browser.current_url}")
            print(f"📄 Page title: {browser.title}")
            
            # Initialize navigation page
            navigation_page = NavigationPage(browser)
            
            # Step 1: Open navigation menu
            print("\n" + "-" * 40)
            print("STEP 1: Opening navigation menu...")
            menu_opened = navigation_page.open_navigation_menu()
            assert menu_opened, "Failed to open navigation menu"
            
            # Step 2: Verify menu items exist
            print("\n" + "-" * 40)
            print("STEP 2: Verifying menu items...")
            items_exist = navigation_page.verify_menu_items_exist()
            assert items_exist, "Not all menu items were found"
            
            # Debug: Print all menu items text
            navigation_page.get_menu_items_text()
            
            # Step 3: Select Accounts
            print("\n" + "-" * 40)
            print("STEP 3: Selecting Accounts...")
            accounts_selected = navigation_page.select_accounts()
            assert accounts_selected, "Failed to select Accounts"
            
            # Step 4: Verify we're on Accounts page
            print("\n" + "-" * 40)
            print("STEP 4: Verifying Accounts page...")
            time.sleep(3)  # Wait for page navigation
            
            # Check URL and page title
            current_url = browser.current_url.lower()
            page_title = browser.title.lower()
            
            print(f"📄 Navigated to URL: {browser.current_url}")
            print(f"📄 Page title: {browser.title}")
            
            # Verify we're on Accounts page
            assert "account" in current_url or "account" in page_title, \
                f"Not on Accounts page. URL: {current_url}, Title: {page_title}"
            
            print("✅ Successfully navigated to Accounts page!")
            
            # Take success screenshot
            browser.save_screenshot("evidence/accounts_navigation_success.png")
            print("📸 Success screenshot saved")
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            # Take failure screenshot
            browser.save_screenshot("evidence/accounts_navigation_failure.png")
            print("📸 Failure screenshot saved")
            raise

    def test_navigation_menu_functionality(self, browser):
        """Test navigation menu functionality in detail"""
        try:
            # Login first
            login_page = LoginPage(browser)
            login_page.navigate_to_login()
            login_page.login("your_username", "your_password")
            time.sleep(5)
            
            navigation_page = NavigationPage(browser)
            
            # Test opening menu
            assert navigation_page.open_navigation_menu(), "Failed to open menu"
            
            # Test that menu items exist
            assert navigation_page.verify_menu_items_exist(), "Menu items missing"
            
            # Test each menu item can be found
            menu_items_to_test = [
                ("Home", navigation_page.HOME_MENU_ITEM),
                ("Accounts", navigation_page.ACCOUNTS_MENU_ITEM),
                ("Opportunities", navigation_page.OPPORTUNITIES_MENU_ITEM),
                ("Quotes", navigation_page.QUOTES_MENU_ITEM)
            ]
            
            for item_name, locator in menu_items_to_test:
                assert navigation_page.is_element_displayed(locator, timeout=5), \
                    f"{item_name} menu item not displayed"
                print(f"✅ {item_name} menu item is present")
            
            print("✅ All navigation menu tests passed!")
            
        except Exception as e:
            print(f"❌ Navigation menu test failed: {e}")
            raise