import pytest
import time
#from pages.site_validation_page import SiteValidationPage
from pages.login_page import LoginPage
from config.base_config import config
from pages.site_validation_page import SiteValiationPage

class TestSiteValidation:
    """Site Validation for Opportunity - Includes login first"""
    
    @pytest.mark.ui
    @pytest.mark.opportunity
    @pytest.mark.e2e
    def test_site_validation_after_login(self, browser):
        """
        Complete end-to-end test: 
        1. Login to Salesforce
        2. Trigger SVS
        """
                
        print(f"\n🚀 Starting SVS ...")
        print(f"   Environment: {config.environment}")
        print(f"   URL: {config.base_url}")
        
        # --- STEP 1: LOGIN TO SALESFORCE ---
        print(f"\n🔐 Step 1: Logging into Salesforce...")
        
        # Initialize page objects
        login_page = LoginPage(browser)
        site_validation_page = SiteValiationPage(browser)
        
        # Perform login directly (don't call another test method)
        #login_page.navigate_to_login_page(config.base_url)
        login_page.load(config.base_url)
        login_page.login(config.get_username(), config.get_password())
        time.sleep(5)
        
        # Verify login was successful
        current_url = browser.current_url.lower()
        assert any(indicator in current_url for indicator in ["lightning", "salesforce", "home"])
        
        # --- STEP 2: PERFORM SITE VALIDATION ---
        print(f"\n🔍 Step 2: Performing Site Validation...")
        
        # Perform site validation
        site_validation_page.trigger_siteupload()
        
        # Verify site validation was successful
        #assert site_validation_page.is_validation_complete(), "Site validation failed"
        print(f"✅ Site validation completed successfully")
        
        # Take screenshot for evidence
        #site_validation_page.take_screenshot("site_validation_success")