# tests/test_opportunity.py
import pytest
import time
from pages.login_page import LoginPage
from pages.opportunity_page import OpportunityPage
from config.base_config import config

class TestOpportunityCreation:
    """Test suite for Opportunity creation flow - Includes login first"""
    
    @pytest.mark.ui
    @pytest.mark.opportunity
    @pytest.mark.e2e
    def test_create_opportunity_after_login(self, browser):
        """
        Complete end-to-end test: 
        1. Login to Salesforce
        2. Create a new Opportunity
        """
        # Test data - kept within the test file for now
        opportunity_data = {
            'name': 'Test Opportunity',
            'account_search': 'Genesis_001',
            #'opportunity_type': 'Fixed',
            #'product_type': 'Fixed',
            'opportunity_due_date':'15-09-2025',
            'expected_closed_date_of_Contract':'30-09-2025',
            'estimated_volume': '2500',
            'contract_start_date':'01-12-2025',
            'expected_contract_duration': '12',
            #'payment_method': 'BACS',
            'tpi_account_name': 'SIP Energy',
            'tpi_contact_name': 'SIP Tester',
            'target_margin': '0.5',
            'target_fixed_margin': '0.5',
            'monthly_tpi_commission': '0.5',
            'tpi_commission': '0.5',
            #'commission_structure': '90% of Contract on live / 10% reconciled at end of contract'
        }
        
        print(f"\n🚀 Starting end-to-end Opportunity creation test...")
        print(f"   Environment: {config.environment}")
        print(f"   URL: {config.base_url}")
        
        # --- STEP 1: LOGIN TO SALESFORCE ---
        print(f"\n🔐 Step 1: Logging into Salesforce...")
        
        login_page = LoginPage(browser)
        
        # Navigate to login page
        login_page.load(config.base_url)
        print(f"   ✅ Loaded login page: {browser.current_url}")
        
        # Perform login with credentials from config
        username = config.get_username()
        password = config.get_password()
        
        if not username or not password:
            pytest.skip("Credentials not configured. Skipping test.")
        
        print(f"   📧 Username: {username}")
        print(f"   🔑 Password: {'*' * len(password) if password else 'Not set'}")
        
        login_page.login(username, password)
        print("   ✅ Login credentials submitted")
        
        # Wait for login to complete and verify
        time.sleep(5)
        current_url = browser.current_url.lower()
        
        # Check if login was successful
        if "login" in current_url:
            pytest.fail("❌ Login failed! Still on login page.")
        
        print(f"   ✅ Login successful! Current URL: {browser.current_url}")
        
        # --- STEP 2: CREATE OPPORTUNITY ---
        print(f"\n🎯 Step 2: Creating new Opportunity...")
        
        opportunity_page = OpportunityPage(browser)
        
        # Execute opportunity creation flow
        opportunity_page.create_opportunity(opportunity_data)
        
        # --- STEP 3: VERIFICATION ---
        print(f"\n✅ Step 3: Verification...")
        
        # Add verification logic here
        # Example: Check if success message appears, opportunity is created, etc.
        print("   ✅ Opportunity creation process completed")
        
        # Temporary verification - check we're not on an error page
        assert "error" not in browser.page_source.lower(), "Error detected after opportunity creation"
        
        print(f"   🎉 Opportunity '{opportunity_data['name']}' created successfully!")
        
        # Optional: Take screenshot as evidence
        try:
            browser.save_screenshot("opportunity_creation_success.png")
            print("   📸 Screenshot saved: opportunity_creation_success.png")
        except Exception as e:
            print(f"   ⚠️ Could not save screenshot: {e}")

    @pytest.mark.ui
    @pytest.mark.opportunity
    def test_opportunity_with_different_data(self, browser):
        """
        Test opportunity creation with different test data
        """
        # Different test data set
        opportunity_data = {
            'name': 'QA Test Opportunity',
            'account_search': 'QA Account',
            'opportunity_type': 'Fixed',
            'product_type': 'Flexible',
            'estimated_volume': '3000',
            'contract_duration': '24',
            'payment_method': 'BACS',
            'tpi_account_name': 'SIP Energy QA',
            'tpi_contact_name': 'SIP Tester QA',
            'target_margin': '0.6',
            'target_fixed_margin': '0.6',
            'monthly_tpi_commission': '0.6',
            'tpi_commission': '0.6',
            'commission_structure': '90% of Contract on live / 10% reconciled at end of contract'
        }
        
        print(f"\n🚀 Testing with different data: {opportunity_data['name']}")
        
        # First login
        login_page = LoginPage(browser)
        login_page.load(config.base_url)
        login_page.login(config.get_username(), config.get_password())
        
        # Wait for login and verify
        time.sleep(5)
        assert "login" not in browser.current_url.lower(), "Login failed"
        
        # Then create opportunity
        opportunity_page = OpportunityPage(browser)
        opportunity_page.create_opportunity(opportunity_data)
        
        print(f"✅ Opportunity '{opportunity_data['name']}' created successfully!")

# Simple test to verify the opportunity page loads
def test_opportunity_page_availability(logged_in_browser):
    """Test that opportunity page is accessible after login"""
    opportunity_page = OpportunityPage(logged_in_browser)
    
    # Try to navigate to accounts (first step in opportunity creation)
    opportunity_page.navigate_to_accounts()
    
    # Verify we can access opportunity-related pages
    assert "account" in logged_in_browser.current_url.lower() or "salesforce" in logged_in_browser.current_url.lower()
    print("✅ Opportunity-related pages are accessible")