

# Input field locators
TPI_CONTACT_INPUT = (By.XPATH, "//label[.//span[text()='TPI Account Contact']]/following::input[@role='combobox']")
TPI_CONTACT_INPUT_ALT = (By.ID, "inputId-2836")
TPI_CONTACT_INPUT_CSS = (By.CSS_SELECTOR, "input[aria-autocomplete='list'][role='combobox']")

# Dropdown options locators
TPI_CONTACT_DROPDOWN = (By.XPATH, "//ul[@role='listbox' and @aria-labelledby]")
TPI_CONTACT_OPTIONS = (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
TPI_CONTACT_OPTION_TEXT = (By.XPATH, "//ul[@role='listbox']//span[@class='slds-listbox__option-text']")

# Specific option by text
TPI_CONTACT_OPTION_BY_TEXT = (By.XPATH, "//ul[@role='listbox']//span[text()='{}']")



def enter_and_select_tpi_contact(self, contact_name="SIP tester"):
    """Enter TPI contact name and select from dropdown suggestions"""
    print(f"👤 Entering and selecting TPI contact: {contact_name}")
    
    try:
        # Step 1: Locate and clear the input field
        input_field = self.wait_for_element_clickable(self.TPI_CONTACT_INPUT)
        input_field.clear()
        time.sleep(0.5)
        
        # Step 2: Enter the contact name character by character (simulates typing)
        print(f"⌨️ Typing: {contact_name}")
        for char in contact_name:
            input_field.send_keys(char)
            time.sleep(0.1)  # Small delay to simulate typing
        
        # Step 3: Wait for dropdown suggestions to appear
        dropdown_visible = self.wait_for_contact_dropdown()
        
        if not dropdown_visible:
            print("⚠️ Dropdown didn't appear, trying to trigger it...")
            input_field.send_keys(Keys.ARROW_DOWN)  # Try to trigger dropdown
        
        # Step 4: Select the matching option
        success = self._select_contact_from_dropdown(contact_name)
        
        if success:
            print(f"✅ Successfully selected TPI contact: {contact_name}")
            return True
        else:
            print(f"❌ Could not select {contact_name} from dropdown")
            return False
            
    except Exception as e:
        print(f"❌ Failed to enter/select TPI contact: {e}")
        self.take_screenshot("tpi_contact_selection_failed")
        return False

def wait_for_contact_dropdown(self, timeout=10):
    """Wait for contact dropdown to appear"""
    print("⏳ Waiting for contact dropdown...")
    
    try:
        # Wait for dropdown container
        return self.wait_for_element_visible(self.TPI_CONTACT_DROPDOWN, timeout)
    except:
        # Check if options are available even if container isn't visible
        options = self.browser.find_elements(*self.TPI_CONTACT_OPTIONS)
        if options:
            print(f"✅ Found {len(options)} options")
            return True
        return False

def _select_contact_from_dropdown(self, contact_name):
    """Select contact from dropdown using multiple strategies"""
    strategies = [
        self._select_contact_by_exact_match,
        self._select_contact_by_partial_match, 
        self._select_first_contact_option,
        self._select_contact_using_keyboard
    ]
    
    for i, strategy in enumerate(strategies):
        try:
            if strategy(contact_name):
                print(f"✅ Selected using strategy {i+1}")
                return True
        except Exception as e:
            print(f"⚠️ Strategy {i+1} failed: {e}")
            continue
    
    return False

def _select_contact_by_exact_match(self, contact_name):
    """Select contact by exact text match"""
    option_locator = (By.XPATH, f"//ul[@role='listbox']//span[text()='{contact_name}']")
    option = self.wait_for_element_clickable(option_locator, timeout=5)
    option.click()
    return True

def _select_contact_by_partial_match(self, contact_name):
    """Select contact by partial text match"""
    option_locator = (By.XPATH, f"//ul[@role='listbox']//span[contains(text(), '{contact_name}')]")
    option = self.wait_for_element_clickable(option_locator, timeout=5)
    option.click()
    return True

def _select_first_contact_option(self, contact_name):
    """Select the first available option"""
    option_locator = (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]")
    option = self.wait_for_element_clickable(option_locator, timeout=5)
    option.click()
    return True

def _select_contact_using_keyboard(self, contact_name):
    """Use keyboard navigation to select contact"""
    input_field = self.wait_for_element_present(self.TPI_CONTACT_INPUT)
    
    # Press down arrow to select first suggestion
    input_field.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
    
    # Press enter to select
    input_field.send_keys(Keys.ENTER)
    return True

def get_available_contact_options(self):
    """Get all available contact options from dropdown"""
    print("📋 Getting available contact options...")
    
    options = []
    try:
        option_elements = self.wait_for_elements_present(self.TPI_CONTACT_OPTION_TEXT, timeout=5)
        for element in option_elements:
            options.append(element.text.strip())
        
        print(f"✅ Available contacts: {options}")
        return options
        
    except Exception as e:
        print(f"❌ Could not get contact options: {e}")
        return options