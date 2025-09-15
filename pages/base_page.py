# pages/base_page.py
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time



class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
    
    def find_element(self, locator):
        """Find a single element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements with explicit wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Click on an element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type_text(self, locator, text):
        """Type text into a field with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def click_and_enter(self, locator, text):
        """First click and Type text into a field with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator)) 
        print(element)  
        element.send_keys(text)
    
    def select_dropdown_option(self, locator, option_text):
        """Select option from dropdown by visible text"""        
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(option_text)
    
    def scroll_to_element(self, locator):
        """Scroll to specific element"""
        element = self.find(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
    
    def wait_for_page_load(self, timeout=10):
        """Wait for page to load completely"""
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def wait_for_element(self, locator, timeout=20):
        """Wait for element to be present and visible"""
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_clickable(self, locator, timeout=20):
        """Wait for element to be clickable - available to all pages"""
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    def is_element_visible(self, locator, timeout=20):
        """Check if element is visible"""
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False
    
    def is_element_clickable(self, locator, timeout=10):
        """Check if element is clickable"""
        try:
            self.wait_for_element_clickable(locator, timeout)
            return True
        except:
            return False
        
    def click_with_javascript(self, locator):
        """Click using JavaScript"""
        try:
            print("🔄 Attempting JavaScript click")
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.browser.execute_script("arguments[0].click();", element)
            print("✅ JavaScript click successful")
            return True
        except Exception as e:
            print(f"❌ JavaScript click failed: {e}")
            raise

    def enter_text_with_javascript(self, locator,text):
        """Enter text using JavaScript"""
        try:
            print(f"🔄 Attempting JavaScript text entry: '{text}'")
            element = self.wait.until(EC.presence_of_element_located(locator))            
            self.browser.execute_script("arguments[0].value = arguments[1];", element, text)
            print("✅ JavaScript text entry successful")
            return True
        except Exception as e:
            print(f"❌ JavaScript text entry failed: {e}")
            raise

    def upload_file_with_javascript11(self, locator, file_path):
        """Upload file using JavaScript by setting the value of file input"""
        try:
            print(f"🔄 Attempting JavaScript file upload: {file_path}")
            
            # Convert to absolute path and ensure it exists
            absolute_path = os.path.abspath(file_path)
            if not os.path.exists(absolute_path):
                raise FileNotFoundError(f"File not found: {absolute_path}")
            
            element = self.wait.until(EC.presence_of_element_located(locator))
            
            # Use JavaScript to set the file path
            self.browser.execute_script(
                "arguments[0].value = arguments[1];", 
                element, 
                absolute_path
            )
            self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
            file_input.send_keys(file_path)
            print("✅ JavaScript file upload successful")
            return True
            
        except Exception as e:
            print(f"❌ JavaScript file upload failed: {e}")
            return False
        

    def upload_file_with_javascript(self, locator, file_path):
        """Click the upload button first, then handle the file input"""
        try:
            # First click the visible upload button
            #element = self.wait.until(EC.element_to_be_clickable(locator))
            #element.click()
        
            print(f"✅ 0 File uploaded: {file_path}")
            # Wait for file dialog to appear (may need to handle OS-level dialog)
            time.sleep(2)
            
            # Now find and interact with the file input
            #file_input = WebDriverWait(self.driver, 10).until(
            #    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            #)
            
            file_input = self.wait.until(EC.element_to_be_clickable(locator))
            print(f"✅1 File uploaded: {file_path}")
            # Use JavaScript to ensure it's interactable
            self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
            file_input.send_keys(file_path)
            print(f"✅ 2 File uploaded: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Upload via button failed: {e}")
            return False
        
    def enter_date(self, locator, date_str, date_format="%d/%m/%Y"):
        """Enter date in input field with validation"""
        try:
            print(f"📅 Entering date: {date_str}")
            
            # Clear and enter date
            element = self.wait_for_element_clickable(locator)
            element.clear()
            element.send_keys(date_str)
            
            # Trigger change event if needed
            #self.browser.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)
            
            print("✅ Date entered successfully")
            return True
            
        except Exception as e:
            print(f"❌ Failed to enter date: {e}")
            return False
        
    
    def select_dropdown_option_by_keyboard(self, locator, text):
        """
        Enter text, press arrow down, and select first dropdown option
        :param locator: Locator of the input field
        :param text: Text to enter in the field
        :return: True if successful, False otherwise
        """
        print(f"⌨️ Entering text and selecting first dropdown: {text}")
        
        try:
            # Wait for and focus on the input field
            input_field = self.wait_for_element_clickable(locator)
            input_field.clear()

            # Enter the text
            input_field.send_keys(text)
            print(f"✅ Entered text: {text}")
            time.sleep(1)  # Wait for dropdown to appear

            # Press arrow down to select first suggestion
            input_field.send_keys(Keys.ARROW_DOWN)
            print("⬇️ Pressed arrow down")
            time.sleep(1)
            
            # Press enter to select
            input_field.send_keys(Keys.ENTER)
            print("✅ Pressed ENTER to select first option")
            time.sleep(1)
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to enter text and select dropdown: {e}")
            return False
        
    def enter_text_robust(self, locator, text, max_attempts=3):
        """Robust text entry with multiple fallback strategies"""
        for attempt in range(max_attempts):
            try:
                print(f"📝 Text entry attempt {attempt + 1} for: '{text}'")
                
                element = self.wait.until(EC.presence_of_element_located(locator))
                
                # Strategy 1: Normal send_keys (clear first)
                try:
                    element.clear()
                    element.send_keys(text)
                    print("✅ Text entered via normal send_keys")
                    return True
                except:
                    pass
                
                # Strategy 2: JavaScript value set
                try:
                    self.driver.execute_script("arguments[0].value = '';", element)  # Clear
                    self.driver.execute_script("arguments[0].value = arguments[1];", element, text)
                    # Trigger events
                    self.driver.execute_script("""
                        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                    """, element)
                    print("✅ Text entered via JavaScript")
                    return True
                except:
                    pass
                
                # Strategy 3: Make element interactable first
                try:
                    self.make_element_interactable(element)
                    element.clear()
                    element.send_keys(text)
                    print("✅ Text entered after making element interactable")
                    return True
                except:
                    pass
                
                # Strategy 4: Click and then send keys
                try:
                    self.driver.execute_script("arguments[0].click();", element)
                    time.sleep(0.5)
                    element.clear()
                    element.send_keys(text)
                    print("✅ Text entered after JavaScript click")
                    return True
                except:
                    pass
                
                time.sleep(1)  # Wait before next attempt
                
            except Exception as e:
                print(f"❌ Attempt {attempt + 1} failed: {e}")
        
        print("❌ All text entry attempts failed")
        return False

    def make_element_interactable(self, element):
        """Make element visible and interactable using JavaScript"""
        try:
            scripts = [
                "arguments[0].style.display = 'block';",
                "arguments[0].style.visibility = 'visible';",
                "arguments[0].style.opacity = '1';",
                "arguments[0].style.position = 'static';",
                "arguments[0].removeAttribute('disabled');",
                "arguments[0].removeAttribute('readonly');",
                "arguments[0].removeAttribute('hidden');",
                "arguments[0].setAttribute('readonly', false);",
                "arguments[0].setAttribute('disabled', false);"
            ]
            
            for script in scripts:
                try:
                    self.driver.execute_script(script, element)
                except:
                    continue
            
            time.sleep(0.5)
            return True
            
        except Exception as e:
            print(f"❌ Failed to make element interactable: {e}")
            return False
        

    