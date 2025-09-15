# tests/step_definitions/test_login_steps.py
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from config.base_config import config
import allure
from selenium.webdriver.common.by import By

# Link to feature file
scenarios('../../features/login.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given("I am on the Salesforce login page")
def go_to_login_page(login_page):
    with allure.step("Navigate to Salesforce login page"):
        login_page.load(config.get_base_url())

@when("the login page loads completely")
def wait_for_login_page(login_page):
    with allure.step("Wait for login page to load"):
        # LoginPage should have a method to wait for elements
        pass

@when(parsers.parse('I attempt to login with username "{username}" and password "{password}"'))
def attempt_login(login_page, username, password):
    with allure.step(f"Attempt login with username: {username}"):
        # Handle environment variables in examples
        if username == '${SF_USERNAME}':
            username = config.get_username()
        if password == '${SF_PASSWORD}':
            password = config.get_password()
        
        login_page.login(username, password)

@then(parsers.parse('I should see the "{result}"'))
def verify_login_result(browser, result):
    with allure.step(f"Verify result: {result}"):
        if result == "home page":
            assert "lightning" in browser.current_url.lower() or "salesforce" in browser.current_url.lower()
        elif result == "error message":
            page_source = browser.page_source.lower()
            assert any(word in page_source for word in ["error", "invalid", "login exception"])
        elif result == "login form":
            assert browser.find_element("id", "username").is_displayed()
            assert browser.find_element("id", "password").is_displayed()

@then('I should see the login form')
def verify_login_form(browser):
    """Verify the login form elements are visible"""
    # Wait for and verify username field
    username_field = browser.find_element(By.ID, "username")
    assert username_field.is_displayed(), "Username field should be visible"
    
    # Wait for and verify password field  
    password_field = browser.find_element(By.ID, "password")
    assert password_field.is_displayed(), "Password field should be visible"
    
    # Verify login button
    login_button = browser.find_element(By.ID, "Login")
    assert login_button.is_displayed(), "Login button should be visible"