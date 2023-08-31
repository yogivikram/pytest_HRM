from hrmhelper.selenium_helper import Selenium_Helper
from selenium.webdriver.common.by import By

class LoginPage(Selenium_Helper):
    email_ele =  (By.XPATH, '//input[@name="username"]')
    password_ele = (By.XPATH, '//input[@name="password"]')
    login_ele = (By.XPATH, '//button')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.webelement_enter(self.email_ele, username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.login_ele)

        