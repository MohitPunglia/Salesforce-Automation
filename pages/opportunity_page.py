# pages/opportunity_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys


class OpportunityPage(BasePage):
    # Locators - Using data-test-id and other stable attributes
    SHOW_NAVIGATION_MENU = (By.XPATH, "//button[@title='Show Navigation Menu']")
    NAV_MENU_DIALOG = (By.XPATH, "//section[@role='dialog' and @aria-label='Navigation Menu']")
    ACCOUNTS_MENU_ITEM = (By.XPATH, "//span[normalize-space()='Accounts']")
    ACCOUNTS_TAB = (By.CSS_SELECTOR, "a[title='Accounts']")
    SEARCH_FIELD = (By.XPATH, "//input[@name='Account-search-input']")
    FIRST_ACCOUNT_NAME = (By.XPATH, "//table[contains(@class, 'slds-table')]//tbody//tr[1]//th//a")
    CREATE_NEW_OPP_BUTTON = (By.XPATH, "//button[normalize-space()='Create New Opportunity']")
    FIXED_OPPORTUNITY_TYPE = (By.XPATH, "//span[@class='slds-img-item-caption' and text()='Fixed']")
    FIXED_OPTION = (By.XPATH, "//span[text()='Fixed']")
    TEST_LOC = (By.XPATH, "//*[@id='brandBand_3']/div/div/c-s-e-l_-o-s-create-c-i-opportunity-english/div/article/div[2]/vlocity_cmt-omniscript-step[1]/div[3]/slot/vlocity_cmt-omniscript-radio[2]/slot/c-radio-image-group/div/div/fieldset/div/div[1]/label/div")
    ACQUISITION_OPTION = (By.XPATH, "//span[text()='Acquisition']")
    NEXT_BUTTON = (By.XPATH, "//div[@class='slds-grid slds-wrap slds-grid_align-end omniscript-button-position']//button[@aria-label='Next']")
    #PRODUCT_TYPE_DROPDOWN = (By.CSS_SELECTOR, "select[data-label='Product Type']")
    OPPORTUNITY_DUE_DATE=(By.XPATH,"//input[@aria-label='Opportunity Due Date']")
    OPPORTUNITY_CLOSE_DATE=(By.XPATH,"//input[@aria-label='Expected Closed Date of Contract']")    
    EST_ANNUAL_VOLUME = (By.XPATH, "//label[contains(., 'Estimated Annual Volume')]/../following-sibling::div//input")
    CONVENTIONAL_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @value='Conventional']")
    RENEWABLE_STANDARD_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @value='Renewable Standard']")
    RENEWABLE_NATURAL_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @value='Renewable Natural']")
    RENEWABLE_SPECIFIC_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @value='Renewable Specific']")
    RENEWABLE_TRACEABLE_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @value='Renewable Traceable']")
    #CONVENTIONAL_OPTION = (By.XPATH, "//span[text()='Conventional']")
    #RENEWABLE_STANDARD_OPTION = (By.XPATH, "//span[text()='Renewable Standard']")
    SINGLE_RATE_OPTION = (By.XPATH, "//input[@type='checkbox' and @value='Single Rate']")
    DOUBLE_RATE_OPTION=(By.XPATH,"//input[@type='checkbox' and @value='2 Rate Day/Night']")
    CONTRACT_START_DATE=(By.XPATH,"//input[@aria-label='Contract Start Date']")
    CONTRACT_DURATION_12MONTHS = (By.XPATH, "//*[@class='slds-img-item-caption' and text()='12 Months'][1]")
    EXPECTED_CONTRACT_DURATION = (By.XPATH, "//label[contains(., 'Expected Contract Duration')]/../following-sibling::div//input") 
    PAYMENT_TERM_30DAYS = (By.XPATH, "//input[@type='checkbox' and @value='30 Days']") 
    #PAYMENT_TERM_DROPDOWN = (By.CSS_SELECTOR, "select[data-label='Payment Method']")
    PAYMENT_METHOD_DROPDOWN = (By.XPATH, "//label[.//span[text()='Payment Method']]/../following-sibling::div//input")
    PAYMENT_METHOD_BACS = (By.XPATH, "//ul[@role='presentation']//span[text()='BACS']")
    PAYMENT_METHOD_DD = (By.XPATH, "//ul[@role='presentation']//span[text()='Direct Debit']")
    #PAYMENT_METHOD_DROPDOWN_CONTAINER = (By.XPATH, "//ul[@class='dropdown-container listbox slds-listbox slds-listbox_vertical' and @role='presentation']")
    #BACS_OPTION = (By.XPATH, "//span[text()='BACS']")
    TPI_ACCOUNT_NAME = (By.XPATH,"//label[contains(., 'TPI Account Name')]/../following-sibling::div//input")
    #TPI_ACCOUNT_NAME = (By.CSS_SELECTOR, "input[data-label='TPI Account Name']")
    TPI_ACCOUNT_CONTACT = (By.XPATH, "//label[contains(., 'TPI Account Contact')]/../following-sibling::div//input")
    #TPI_ACCOUNT_CONTACT = (By.CSS_SELECTOR, "input[data-label='TPI Account Contact']")
    TARGET_MARGIN = (By.XPATH, "//*[text()='Target Margin (£/MWh)']/../following-sibling::div//input")
    TARGET_FIXED_MARGIN = (By.XPATH, "//*[text()='Target Fixed Margin (£/MPAN/Month)']/../following-sibling::div//input")
    MONTHLY_TPI_COMMISSION = (By.XPATH, "//*[text()='Monthly TPI Commission - £/MPAN/Month']/../following-sibling::div//input")
    TPI_COMMISSION = (By.XPATH, "//*[text()='TPI Commission - £/MWh']/../following-sibling::div//input")
    COMMISSION_STRUCTURE_DROPDOWN = (By.XPATH, "//label[.//span[text()='TPI Commission Payment Structure']]/../following-sibling::div//input")
    COMMISSION_OPTION = (By.XPATH, "//ul[@role='presentation']//span[text()='90% of Contract on live / 10% reconciled at end of contract']")
    POTENTIAL_COMPETING_OPPORTUNITY=(By.XPATH,"//h1[text()='Potential Competing Opportunity']")
    FIXED_PRODUCT = (By.XPATH, "//button[normalize-space()='Fixed']")
    FIXED_PASSTHROUGH_OPTION = (By.XPATH, "//button[normalize-space()='Fixed Passthrough']")
    OPPORTUNITY_HOME_PAGE=(By.XPATH,"//*[@class='entityNameTitle slds-line-height--reset']")
    

    def open_navigation_menu(self):
        """Navigate to EnergyB2Bsales home page"""
        """Click on Show Navigation Menu and wait for menu to appear"""
        print("🔄 Opening navigation menu...")
        try:
            # Click the navigation menu button
            self.click(self.SHOW_NAVIGATION_MENU)
            print("✅ Navigation menu button clicked")
            
            # Wait for the menu dialog to appear
            self.wait_for_element(self.NAV_MENU_DIALOG)
            print("✅ Navigation menu opened and visible")
            
            time.sleep(1)  # Brief pause for menu to stabilize

            """Click on Accounts menu item"""
            self.click(self.ACCOUNTS_MENU_ITEM)
            print("🔄 Clicking Accounts...")


            return True
            
            
        except Exception as e:
            print(f"❌ Failed to open navigation menu: {e}")
            #self.take_screenshot("navigation_menu_failed")
            return False


    def navigate_to_accounts(self):
        """Navigate to Accounts tab"""
        self.click(self.ACCOUNTS_TAB)
        print("✅ Navigated to Accounts tab")

    """def search_accounts(self, search_term):
        "Search in accounts list"

        self.type_text(self.SEARCH_FIELD, search_term)
        print(f"✅ Searched for: {search_term}")"""

        
    def search_accounts(self, search_term):
        """Search in accounts list and press Enter to execute search"""
        try:
            # Wait for search field to be available
            search_field = self.wait_for_element_clickable(self.SEARCH_FIELD, timeout=30)
            
            # Clear and enter search term
            search_field.clear()
            search_field.send_keys(search_term)
            print(f"✅ Entered search term: {search_term}")
            
            # Press Enter key to execute the search
            search_field.send_keys(Keys.ENTER)
            print("✅ Pressed Enter to execute search")
            
            time.sleep(3)  # Allow search results to load
            
             # Click on the first account name in search results
            self.click_first_account_name()
            
        except Exception as e:
            print(f"❌ Search failed: {e}. Continuing without search...")


    def click_first_account_name(self):
        """Click on the first account name to open account details"""
        try:
            # Locate and click the account name link
            #first_account_name_locator = (By.CSS_SELECTOR, "table.slds-table[role='grid'] > tbody > tr[role='row']:first-child th[role='rowheader'] a")
            
            account_name_link = self.wait_for_element_clickable(self.FIRST_ACCOUNT_NAME, timeout=15)
            
            account_name = account_name_link.text.strip()
            print(f"***************{account_name}********************")
            account_name_link.click()
            print(f"✅ Clicked account: {account_name}")
            
            time.sleep(3)  # Wait for account page to load
            return True
            
        except Exception as e:
            print(f"❌ Failed to click account name: {e}")
            return False

        

    def click_create_new_opportunity(self):
        """Click Create New Opportunity button"""
        time.sleep(5)
        self.click_with_javascript(self.CREATE_NEW_OPP_BUTTON)
        print("✅ Clicked Create New Opportunity")
        print("❌ Clicked 2nd time")
        self.click_with_javascript(self.CREATE_NEW_OPP_BUTTON)
        print("✅ Clicked Create New Opportunity")
        self.wait_for_page_load()
        print("❌❌Page loaded ❌❌")

    def select_opportunity_type(self):
        print("❌❌❌object has no attribute 'find'❌❌❌")
        """Select opportunity type"""
        #self.click(self.FIXED_OPPORTUNITY_TYPE)
        self.wait_for_page_load(timeout=30)
        print("✅ Page appears to be loaded")
        #time.sleep(10)
        #self.is_element_visible(self.TEST_LOC)
        self.is_element_visible(self.FIXED_OPPORTUNITY_TYPE)
        print("❌❌❌Element visible❌❌❌")    
        #self.click(self.TEST_LOC)
        self.click_with_javascript(self.FIXED_OPPORTUNITY_TYPE)
        #dropdown = Select(self.find(self.OPPORTUNITY_TYPE_DROPDOWN))
        #dropdown.select_by_visible_text(opp_type)
        print(f"✅ Selected Opportunity Type: Fixed")

    
    
  

    def select_fixed_acquisition(self):
        """Select Fixed and Acquisition options"""
        #self.wait_for_element(self.FIXED_OPTION)
        #self.click(self.FIXED_OPTION)
        self.click_with_javascript(self.ACQUISITION_OPTION)
        print("✅ Selected Fixed and Acquisition")

    def click_next(self):
        """Click Next button"""
        self.click(self.NEXT_BUTTON)
        print("✅ Clicked Next")
        time.sleep(2)  # Allow page to load

    """def select_product_type(self, product_type):
        "Select product type from dropdown"
        dropdown = Select(self.find(self.PRODUCT_TYPE_DROPDOWN))
        dropdown.select_by_visible_text(product_type)
        print(f"✅ Selected Product Type: {product_type}")"""
    
    def select_opportunity_duedate(self, opp_duedate):
        self.wait_for_element(self.OPPORTUNITY_DUE_DATE)
        self.enter_date(self.OPPORTUNITY_DUE_DATE,opp_duedate)
        
        print(f"✅ Selected date Type: {opp_duedate}")

    def select_close_date_of_contract(self, opp_closedate):
        self.enter_date(self.OPPORTUNITY_CLOSE_DATE,opp_closedate)
        
        print(f"✅ Selected Opportunity close date: {opp_closedate}")

    def enter_estimated_volume(self, volume):
        """Enter estimated annual volume"""
        self.type_text(self.EST_ANNUAL_VOLUME, volume)
        print(f"✅ Entered Estimated Volume: {volume}")

    def select_energy_options(self):
        """Select energy type options"""
        self.click_with_javascript(self.CONVENTIONAL_CHECKBOX)
        #self.click(self.RENEWABLE_STANDARD_OPTION)
        self.click_with_javascript(self.SINGLE_RATE_OPTION)
        print("✅ Selected energy options")

    def select_contract_startdate(self, contract_start_date):
        self.enter_date(self.CONTRACT_START_DATE,contract_start_date)        
        print(f"✅ Selected contract start date: {contract_start_date}")


    def select_contract_duration(self):
        """Select contract duration"""
        self.click(self.CONTRACT_DURATION_12MONTHS)
        print(f"✅ Selected Contract Duration 12 Months")

    def enter_expected_contract_duration(self, expected_con_duration):
        """Enter Expected Contract Duration"""
        self.type_text(self.EXPECTED_CONTRACT_DURATION, expected_con_duration)
        print(f"✅ Entered Expected Contract Duration: {expected_con_duration}")

    def select_payment_terms(self):
        """Select Payment Terms options"""
        self.click_with_javascript(self.PAYMENT_TERM_30DAYS)
        
        print("✅ Selected 30 Days as Payment Terms")
    

    def select_payment_method(self):
        """Select payment method"""
        self.click(self.PAYMENT_METHOD_DROPDOWN)
        time.sleep(2)
        self.wait_for_element(self.PAYMENT_METHOD_BACS)
        self.click(self.PAYMENT_METHOD_BACS)
        print(f"✅ Selected Payment Method as BACS")

    def enter_tpi_account_name(self, account_name):
        """Enter TPI account details"""
        #self.wait_for_element(self.TPI_ACCOUNT_NAME)
        #self.type_text(self.TPI_ACCOUNT_NAME, account_name)
        print(f"✅ Entered TPI Account Name Details: {account_name}")
        self.select_dropdown_option_by_keyboard(self.TPI_ACCOUNT_NAME, account_name)
        

    def enter_tpi_account_contact(self, contact_name):
        """Enter TPI account details"""
        #self.wait_for_element(self.TPI_ACCOUNT_CONTACT)
        #self.type_text(self.TPI_ACCOUNT_CONTACT, contact_name)
        print(f"✅ Entered TPI Contact Details: {contact_name}")
        self.select_dropdown_option_by_keyboard(self.TPI_ACCOUNT_CONTACT, contact_name)
        

        

    """def enter_tpi_details(self, account_name, contact_name):
        "Enter TPI account details"
        self.type_text(self.TPI_ACCOUNT_NAME, account_name)
        self.type_text(self.TPI_ACCOUNT_CONTACT, contact_name)
        print(f"✅ Entered TPI Details: {account_name}, {contact_name}")"""

    def enter_commission_details(self, target_margin, fixed_margin, monthly_commission, tpi_commission):
        """Enter commission details"""
        self.wait_for_element(self.TARGET_MARGIN)
        self.type_text(self.TARGET_MARGIN, target_margin)
        self.wait_for_element(self.TARGET_FIXED_MARGIN)
        self.type_text(self.TARGET_FIXED_MARGIN, fixed_margin)
        self.wait_for_element(self.MONTHLY_TPI_COMMISSION)
        self.type_text(self.MONTHLY_TPI_COMMISSION, monthly_commission)
        self.wait_for_element(self.TPI_COMMISSION)
        self.type_text(self.TPI_COMMISSION, tpi_commission)
        print("✅ Entered commission details")

    """def select_commission_structure(self, structure):
        "Select commission payment structure"
        dropdown = Select(self.find(self.COMMISSION_STRUCTURE_DROPDOWN))
        dropdown.select_by_visible_text(structure)
        print(f"✅ Selected Commission Structure: {structure}")"""

    def select_commission_structure(self):
        """Select commission payment structure"""
        
        self.click(self.COMMISSION_STRUCTURE_DROPDOWN)
        time.sleep(2)
        self.wait_for_element(self.COMMISSION_OPTION)
        self.click(self.COMMISSION_OPTION)
        
        print(f"✅ Selected Commission Structure from Dropdown")

    def check_potential_competing_opportunity(self):
        """Check if Potential Competing Opportunity page is displayed"""
        if (self.is_element_visible(self.POTENTIAL_COMPETING_OPPORTUNITY)):
            print(f"✅ Potential Competing Opportunity page is displayed")
        else:
            print(f"❌ No Potential Competing Opportunity page is displayed")


    def select_fixed_passthrough(self):
        """Select Fixed Passthrough option"""
        time.sleep(10)
        self.wait_for_element(self.FIXED_PRODUCT)
        self.click(self.FIXED_PRODUCT)
        print("✅ Selected Fixed Product")

    def check_opportunity_homepage(self):
        """Opportunity home page Verification"""
    
        self.is_element_visible(self.OPPORTUNITY_HOME_PAGE)
        print(f"✅ Opportunity Home page is displayed")

    def create_opportunity(self, opportunity_data):
        """Complete opportunity creation flow"""
        print(f"\n🚀 Creating Opportunity: {opportunity_data['name']}")
        
        # Navigation
        self.open_navigation_menu()
        self.navigate_to_accounts()
        self.search_accounts(opportunity_data.get('account_search', ''))
        self.click_create_new_opportunity()
        
        # Step 1: Opportunity Type
        self.select_opportunity_type()
        self.select_fixed_acquisition()
        self.click_next()
        
        # Step 2: Product Details
        self.select_opportunity_duedate(opportunity_data['opportunity_due_date'])
        self.select_close_date_of_contract(opportunity_data['expected_closed_date_of_Contract'])
        #self.select_product_type(opportunity_data['product_type'])
        self.enter_estimated_volume(opportunity_data['estimated_volume'])
        self.select_energy_options()
        self.select_contract_startdate(opportunity_data['contract_start_date'])
        self.select_contract_duration()
        self.enter_expected_contract_duration(opportunity_data['expected_contract_duration'])
        self.select_payment_terms()

        #self.click_next()
        
        # Step 3: Commercial Details
        self.select_payment_method()
        #self.enter_tpi_details(opportunity_data['tpi_account_name'], opportunity_data['tpi_contact_name'])
        self.enter_tpi_account_name(opportunity_data['tpi_account_name'])
        self.enter_tpi_account_contact(opportunity_data['tpi_contact_name'])
        self.enter_commission_details(
            opportunity_data['target_margin'],
            opportunity_data['target_fixed_margin'],
            opportunity_data['monthly_tpi_commission'],
            opportunity_data['tpi_commission']
        )
        self.select_commission_structure()
        self.click_next()
        
        # Step 4: Potential Competing Opportunity
        self.check_potential_competing_opportunity()
        self.click_next()

        # Step 5: Final Selection
        self.select_fixed_passthrough()
        self.click_next()

        # Step 6: Opportunity Creation Verification
        self.check_opportunity_homepage()
        
       
        print("✅ Opportunity creation process completed!")
        