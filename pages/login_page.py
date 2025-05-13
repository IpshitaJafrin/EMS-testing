from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    URL = f"{BASE_URL}/administer"

    USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign In']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)