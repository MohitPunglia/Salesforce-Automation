# pages/navigation_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class NavigationPage(BasePage):
    # Exact locators from the HTML provided
    SHOW_NAVIGATION_MENU = (By.XPATH, "//button[@title='Show Navigation Menu']")
    
    # Navigation menu container (wait for this to be visible)
    NAV_MENU_DIALOG = (By.XPATH, "//section[@role='dialog' and @aria-label='Navigation Menu']")
    
    # Menu items - using data-label attribute for precise targeting
    ACCOUNTS_MENU_ITEM = (By.XPATH, "//a[@role='menuitem' and @data-label='Accounts']")
    HOME_MENU_ITEM = (By.XPATH, "//a[@role='menuitem' and @data-label='Home']")
    OPPORTUNITIES_MENU_ITEM = (By.XPATH, "//a[@role='menuitem' and @data-label='Opportunities']")
    QUOTES_MENU_ITEM = (By.XPATH, "//a[@role='menuitem' and @data-label='Quotes']")
    
    # Alternative locators using text content
    ACCOUNTS_MENU_TEXT = (By.XPATH, "//span[@class='menuLabel' and text()='Accounts']")
    
    def open_navigation_menu(self):
        """Click on Show Navigation Menu and wait for menu to appear"""
        print("🔄 Opening navigation menu...")
        try:
            # Click the navigation menu button
            self.click_with_retry(self.SHOW_NAVIGATION_MENU, retries=3, delay=2)
            print("✅ Navigation menu button clicked")
            
            # Wait for the menu dialog to appear
            self.wait_for_element_visible(self.NAV_MENU_DIALOG, timeout=10)
            print("✅ Navigation menu opened and visible")
            
            time.sleep(1)  # Brief pause for menu to stabilize
            return True
            
        except Exception as e:
            print(f"❌ Failed to open navigation menu: {e}")
            self.take_screenshot("navigation_menu_failed")
            return False

    def select_menu_item(self, menu_item_locator, item_name):
        """Select a specific menu item"""
        print(f"🔄 Selecting {item_name} from menu...")
        try:
            # Wait for menu item to be clickable
            self.wait_for_element_clickable(menu_item_locator, timeout=10)
            
            # Click the menu item
            self.click_with_retry(menu_item_locator, retries=2, delay=1)
            print(f"✅ {item_name} menu item clicked")
            
            # Wait for menu to close (optional)
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"❌ Failed to select {item_name}: {e}")
            return False

    def select_accounts(self):
        """Select Accounts from navigation menu"""
        return self.select_menu_item(self.ACCOUNTS_MENU_ITEM, "Accounts")

    def select_opportunities(self):
        """Select Opportunities from navigation menu"""
        return self.select_menu_item(self.OPPORTUNITIES_MENU_ITEM, "Opportunities")

    def select_quotes(self):
        """Select Quotes from navigation menu"""
        return self.select_menu_item(self.QUOTES_MENU_ITEM, "Quotes")

    def select_home(self):
        """Select Home from navigation menu"""
        return self.select_menu_item(self.HOME_MENU_ITEM, "Home")

    def navigate_to_accounts_via_menu(self):
        """Complete flow: Open menu and select Accounts"""
        print("🚀 Navigating to Accounts via navigation menu...")
        
        # Open the navigation menu
        if not self.open_navigation_menu():
            return False
        
        # Select Accounts
        if not self.select_accounts():
            # Try alternative locator if first attempt fails
            print("🔄 Trying alternative Accounts locator...")
            return self.select_menu_item(self.ACCOUNTS_MENU_TEXT, "Accounts")
        
        return True

    def verify_menu_items_exist(self):
        """Verify all expected menu items are present"""
        print("🔍 Verifying navigation menu items...")
        
        menu_items = {
            "Home": self.HOME_MENU_ITEM,
            "Accounts": self.ACCOUNTS_MENU_ITEM,
            "Opportunities": self.OPPORTUNITIES_MENU_ITEM,
            "Quotes": self.QUOTES_MENU_ITEM
        }
        
        all_found = True
        
        for item_name, locator in menu_items.items():
            try:
                if self.is_element_displayed(locator, timeout=5):
                    print(f"✅ {item_name} menu item found")
                else:
                    print(f"❌ {item_name} menu item not found")
                    all_found = False
            except:
                print(f"❌ {item_name} menu item not found")
                all_found = False
        
        return all_found

    def get_menu_items_text(self):
        """Get text of all menu items for debugging"""
        print("📋 Getting all menu items text...")
        
        # Find all menu labels
        menu_labels = self.browser.find_elements(By.XPATH, "//span[@class='menuLabel']")
        
        for i, label in enumerate(menu_labels):
            print(f"   {i+1}. '{label.text}'")
        
        return [label.text for label in menu_labels]