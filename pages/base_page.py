from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """Click an element."""
        try:
            element = self.driver.find_element(*by_locator)
            element.click()
        except NoSuchElementException:
            raise Exception(f"Element not found: {by_locator}")
        except WebDriverException as e:
            raise Exception(f"Error while clicking element: {e}")

    def enter_text(self, by_locator, text):
        """Enter text into an input field."""
        try:
            element = self.driver.find_element(*by_locator)
            element.clear()  # Clear any existing text before sending new text
            element.send_keys(text)
        except NoSuchElementException:
            raise Exception(f"Element not found: {by_locator}")
        except WebDriverException as e:
            raise Exception(f"Error while entering text: {e}")

    def get_title(self):
        """Get the page title."""
        return self.driver.title

    def wait_for_element(self, by_locator, timeout=10):
        """Wait for an element to be visible."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                element = self.driver.find_element(*by_locator)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                time.sleep(0.5)  # Retry until timeout
        raise Exception(f"Element not found or visible after {timeout} seconds: {by_locator}")
