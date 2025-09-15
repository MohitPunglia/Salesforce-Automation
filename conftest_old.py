# conftest.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@pytest.fixture(scope="function")  # This fixture runs for each test
def browser():
    # Setup: Before the test
    print("\nStarting browser...")
    
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    # chrome_options.add_argument("--headless")  # Uncomment to run without GUI (faster)
    
    # Use webdriver-manager to automatically handle ChromeDriver
    service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # This gives the driver instance to the test
    yield driver
    
    # Teardown: After the test
    print("\nQuitting browser...")
    driver.quit()

def pytest_runtest_setup(item):
        """Skip tests if credentials are not configured"""
        if item.get_closest_marker('requires_credentials'):
            from config.base_config import config
            if not config.get_username() or not config.get_password():
                pytest.skip("Credentials not configured in .env file")


# Add this fixture for screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Check if test has browser fixture
        if hasattr(item, 'funcargs') and 'browser' in item.funcargs:
            browser = item.funcargs['browser']
            try:
                # Take screenshot
                screenshot = browser.get_screenshot_as_png()
                # Attach to Allure report
                allure.attach(
                    screenshot,
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # Attach page source
                page_source = browser.page_source
                allure.attach(
                    page_source,
                    name="page_source_on_failure", 
                    attachment_type=allure.attachment_type.HTML
                )
                
            except Exception as e:
                print(f"Failed to capture evidence: {e}")


# Add this fixture for screenshots on success too
@pytest.fixture(autouse=True)
def capture_evidence(browser, request):
    """Capture screenshot for every test"""
    yield
    # Capture after test completes
    if hasattr(request.node, 'rep_call') and request.node.rep_call.passed:
        try:
            screenshot = browser.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"screenshot_{request.node.name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture success screenshot: {e}")
    

