# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SiteValiationPage(BasePage):
    # Locators - these are the addresses of elements on the page
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "Login")
    MPAN_TAB = (By.ID,"flexipage_tabmpans__item")
    OPPORTUNITY_HOME_PAGE = (By.XPATH,"//*[@class='entityNameTitle slds-line-height--reset']")
    SITE_UPLOAD_BUTTON = (By.XPATH, "//button[normalize-space()='Site Upload']")
    #SITE_UPLOAD_COMMETNS = (By.XPATH, "//label[contains(., 'Comment')]/../div")
    SITE_UPLOAD_COMMETNS = (By.XPATH, "//*[@class='slds-form-element__control slds-grow' and @type='text']")    
    UPLOAD_FILE_BUTTON = (By.XPATH, "//span[@class='slds-file-selector__button slds-button slds-button_neutral']")
    UPLOAD_BUTTON = ((By.CSS_SELECTOR, "input[type='file']"))
    FILE_PATH = "C:\\Users\\PungliaM\\Downloads\\MPAN - Fixed HH new (1).csv"
    

        
    def load(self):
        """Navigate to the login page"""
        self.browser.get("https://smartestenergy--cpgsitqa.sandbox.lightning.force.com/lightning/r/Opportunity/006Ae00000jc0l3IAA/view?ws=%2Flightning%2Fr%2FAccount%2F001Ae00000ZK0kaIAD%2Fview")

        """Opportunity home page Verification"""
    
        self.is_element_visible(self.OPPORTUNITY_HOME_PAGE)
        print(f"✅ Opportunity Home page is displayed")

    def navigate_to_mpan_tab(self):
        print(f"✅ Start process inside method")
        #self.wait_for_element(self.MPAN_TAB)
        #self.click(self.MPAN_TAB)
        print(f"✅ MPAN tab selected")
        self.wait_for_element(self.SITE_UPLOAD_BUTTON)
        self.click(self.SITE_UPLOAD_BUTTON)
        print(f"✅ Site upload button clicked")
        #search_field=self.wait_for_element_clickable(self.SITE_UPLOAD_COMMETNS)
        # Clear and enter search term
        #search_field.clear()
        #time.sleep(1)
        #search_field.send_keys('TEST')
        #self.enter_text_with_javascript(self.SITE_UPLOAD_COMMETNS,'Test')
        #print(f"✅ Comments added")
        #time.sleep(5)
        #print(f"File path is {self.FILE_PATH}")
        
        #self.upload_file_with_javascript(self.UPLOAD_BUTTON,self.FILE_PATH)
        #print(f"clicked file path {self.FILE_PATH}")
        #self.click_and_enter(self.UPLOAD_BUTTON,self.FILE_PATH)
        #self.type_text(self.UPLOAD_FILE_BUTTON,self.FILE_PATH)
        #time.sleep(20)

        #self.wait_for_element(self.SITE_UPLOAD_COMMETNS)
        #self.type_text(self.SITE_UPLOAD_COMMETNS,"Test-Site upload")

    def enter_field_text(self, field_name, text):
        """Enter text in a specific field with robust error handling"""
        self.enter_text_robust(self.SITE_UPLOAD_COMMETNS, text)

    def upload_files(self, file_path):
        """Upload a file to Salesforce using JavaScript workaround"""
        try:
            # Find the file input element (even if hidden)
            file_inputs = self.UPLOAD_FILE_BUTTON
            
            if not file_inputs:
                raise Exception("No file input element found")
            
            # Use JavaScript to make the element visible and set it to interactable state
            self.driver.execute_script("""
                arguments[0].style.display = 'block';
                arguments[0].style.visibility = 'visible';
                arguments[0].style.height = '20px';
                arguments[0].style.width = '200px';
                arguments[0].style.opacity = 1;
                arguments[0].style.position = 'static';
                arguments[0].removeAttribute('disabled');
                arguments[0].removeAttribute('readonly');
            """, file_inputs[0])
            
            # Wait briefly for the element to become interactable
            time.sleep(1)
            
            # Now send the file path
            file_inputs[0].send_keys(file_path)
            print(f"✅ File uploaded: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ File upload error: {e}")
            return False
        
    def upload_file_via_button(self, file_path):
        """Click the upload button first, then handle the file input"""
        try:
            # First click the visible upload button
            self.click(self.UPLOAD_FILE_BUTTON)
            print(f"✅ 0 File uploaded: {file_path}")
            # Wait for file dialog to appear (may need to handle OS-level dialog)
            time.sleep(2)
            
            # Now find and interact with the file input
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            )
            print(f"✅1 File uploaded: {file_path}")
            # Use JavaScript to ensure it's interactable
            self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
            file_input.send_keys(file_path)
            print(f"✅ 2 File uploaded: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Upload via button failed: {e}")
            return False
    

    def trigger_siteupload(self):
        """Complete Site Upload creation flow"""
        print(f"\n🚀 SVS Process")
        
        # Navigation
        self.load()
        print(f"\n Next Process")
        self.navigate_to_mpan_tab()
        self.enter_field_text(self.SITE_UPLOAD_COMMETNS,'Test')
        #self.upload_file_via_button(self.FILE_PATH)
        time.sleep(20)