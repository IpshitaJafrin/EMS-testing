# conftest.py

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.helper import take_screenshot
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD

# ----------------------------
# Pytest-html integration
# ----------------------------

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser", None)
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            if screenshot_path and os.path.exists(screenshot_path):
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra

# ----------------------------
# Fixtures
# ----------------------------

@pytest.fixture(scope="function")
def browser():
    """Initialize WebDriver"""
    options = Options()
    # Uncomment to run in headless mode:
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_browser(browser):
    """Login before each test using LoginPage"""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    return browser
