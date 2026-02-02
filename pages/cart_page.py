from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    cart_button = (By.ID, "shopping_cart_container")
    cart_items = (By.CLASS_NAME, "inventory_item_name")

    def click_cart(self):
        self.click(self.cart_button)
        
    def get_cart_items(self):
        elements = self.driver.find_elements(*self.cart_items)
        return [el.text for el in elements]
