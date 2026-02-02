from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    checkout_button = (By.XPATH, "//button[@id='checkout']")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    confirmation_msg = (By.CLASS_NAME, "complete-header")

    def checkout(self):
        self.click(self.checkout_button)

    def fill_information(self, first, last, postal):
        self.type(self.first_name, first)
        self.type(self.last_name, last)
        self.type(self.postal_code, postal)
        self.click(self.continue_btn)

    def finish_checkout(self):
        self.click(self.finish_btn)

    def get_confirmation_message(self):
        return self.get_text(self.confirmation_msg)
