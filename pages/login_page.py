from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import get_config

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(get_config("app", "base_url"))

    def login(self, user, pwd):
        self.type(self.username, user)
        self.type(self.password, pwd)
        self.click(self.login_button)
