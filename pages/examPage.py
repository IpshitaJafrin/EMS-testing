from selenium.webdriver.common.by import By
from .base_page import BasePage

class ExamPage(BasePage):
    URL = f"{BASE_URL}/administer/ExamTemplates/index"

    NEW_TEMPLET = (By.XPATH, "//a[normalize-space()='New Template']")
    templet_name = (By.XPATH, "//input[@id='examination_name']")
    campus = (By.XPATH, "//select[@id='campus_id']")
    shift = (By.XPATH, "//select[@id='shift_id']")



    def open(self):
        self.driver.get(self.URL)

    def enter_exam_name(self, exam_name):
        self.driver.find_element(*self.NEW_TEMPLET).click()
        self.driver.find_element(*self.templet_name).send_keys(exam_name)
