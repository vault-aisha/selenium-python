from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HeaderPage(BasePage):
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)
