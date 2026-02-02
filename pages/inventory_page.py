from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    add_to_cart_buttons = (By.CSS_SELECTOR, ".inventory_item button")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    item_names = (By.CLASS_NAME, "inventory_item_name")

    def add_all_items_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        for btn in buttons:
            btn.click()

    def go_to_cart(self):
        self.click(self.cart_icon)

    def get_all_item_names(self):
        elements = self.driver.find_elements(*self.item_names)
        return [el.text for el in elements]
