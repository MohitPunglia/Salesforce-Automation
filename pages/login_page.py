# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators - these are the addresses of elements on the page
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "Login")
    
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
    
    def load(self, url):
        """Navigate to the login page"""
        self.browser.get(url)
    
    def login(self, username, password):
        """Perform login with given credentials"""
        # Wait for and enter username
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        username_field.clear()
        username_field.send_keys(username)
        
        # Enter password
        password_field = self.browser.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()