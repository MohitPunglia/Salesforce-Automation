
# conftest.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

@pytest.fixture(scope="function")  # This fixture runs for each test
def browser():
    # Setup: Before the test
    print("\nStarting browser...")

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    # chrome_options.add_argument("--headless")  # Uncomment to run without GUI (faster)

    # Use webdriver-manager to automatically handle ChromeDriver
    service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set implicit wait
    driver.implicitly_wait(10)

    # This gives the driver instance to the test
    yield driver

    # Teardown: After the test
    print("\nQuitting browser...")
    driver.quit()

@pytest.fixture(autouse=True)
def clear_cookies_before_test(browser):
    """Clear cookies before each test runs"""
    print("🧹 Clearing browser cookies and local storage...")
    try:
        # Clear cookies
        browser.delete_all_cookies()
        print("✅ Cookies cleared")

        # Clear local storage and session storage (optional)
        browser.execute_script("window.localStorage.clear();")
        browser.execute_script("window.sessionStorage.clear();")
        print("✅ Local storage cleared")

    except Exception as e:
        print(f"⚠️ Could not clear browser data: {e}")

    yield

    # Optional: Clear cookies after test as well for extra cleanup
    try:
        browser.delete_all_cookies()
    except:
        pass

def pytest_runtest_setup(item):
    """Skip tests if credentials are not configured"""
    if item.get_closest_marker('requires_credentials'):
        from config.base_config import config
        if not config.get_username() or not config.get_password():
            pytest.skip("Credentials not configured in .env file")

# Add this fixture for screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots and evidence on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        # Check if test has browser fixture
        if hasattr(item, 'funcargs') and 'browser' in item.funcargs:
            browser = item.funcargs['browser']
            try:
                # Take screenshot
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                test_name = item.name

                screenshot = browser.get_screenshot_as_png()
                # Attach to Allure report
                allure.attach(
                    screenshot,
                    name=f"screenshot_failure_{test_name}_{timestamp}",
                    attachment_type=allure.attachment_type.PNG
                )

                # Save screenshot to file as well
                try:
                    browser.save_screenshot(f"evidence/failure_{test_name}_{timestamp}.png")
                    print(f"📸 Screenshot saved: evidence/failure_{test_name}_{timestamp}.png")
                except:
                    pass

                # Attach page source
                page_source = browser.page_source
                allure.attach(
                    page_source,
                    name=f"page_source_failure_{test_name}_{timestamp}",
                    attachment_type=allure.attachment_type.HTML
                )

                # Attach browser logs
                try:
                    logs = browser.get_log('browser')
                    if logs:
                        allure.attach(
                            str(logs),
                            name=f"browser_logs_{test_name}_{timestamp}",
                            attachment_type=allure.attachment_type.TEXT
                        )
                except:
                    pass

                # Attach current URL
                current_url = browser.current_url
                allure.attach(
                    current_url,
                    name=f"current_url_{test_name}_{timestamp}",
                    attachment_type=allure.attachment_type.TEXT
                )

            except Exception as e:
                print(f"Failed to capture evidence: {e}")

# Add this fixture for screenshots on success too
@pytest.fixture(autouse=True)
def capture_evidence(browser, request):
    """Capture screenshot for every test (success and failure)"""
    # Store test start time
    request.node._start_time = time.time()

    yield

    # Capture after test completes
    try:
        test_name = request.node.name
        duration = time.time() - request.node._start_time
        status = "passed" if not hasattr(request.node, 'rep_call') or request.node.rep_call.passed else "failed"

        screenshot = browser.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=f"screenshot_{test_name}_{status}",
            attachment_type=allure.attachment_type.PNG
        )

        # Save success screenshots to file
        if status == "passed":
            try:
                browser.save_screenshot(f"evidence/success_{test_name}_{time.strftime('%Y%m%d_%H%M%S')}.png")
            except:
                pass

    except Exception as e:
        print(f"Failed to capture evidence: {e}")

# Optional: Add session-level fixture for global setup/teardown
@pytest.fixture(scope="session", autouse=True)
def global_setup():
    """Global setup before all tests"""
    print("\n" + "="*60)
    print("🚀 Starting test session")
    print("="*60)

    yield

    # Global teardown after all tests
    print("\n" + "="*60)
    print("✅ Test session completed")
    print("="*60)

# Optional: Add module-level fixture
@pytest.fixture(scope="module", autouse=True)
def module_setup():
    """Setup before each test module"""
    print(f"\n📦 Starting test module")
    yield
    print(f"📦 Test module completed")

# Optional: Add test failure count tracking
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    """Print test summary at the end"""
    outcome = yield
    print(f"\n📊 Test Summary: {session.testsfailed} failed, {session.testscollected - session.testsfailed} passed")
