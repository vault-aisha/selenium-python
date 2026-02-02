import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.header_page import HeaderPage

def test_simple_checkout_e2e(setup):
    driver = setup

    # -------------------------
    # 1️⃣ Login
    # -------------------------
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # -------------------------
    # 2️⃣ Add items to cart
    # -------------------------
    inventory = InventoryPage(driver)
    inventory.add_all_items_to_cart()  # Add all items

    # -------------------------
    # 3️⃣ Go to Cart
    # -------------------------
    # inventory.go_to_cart()

    # -------------------------
    # 4️⃣ Checkout
    # -------------------------
    cart = CartPage(driver)
    cart.click_cart ()  # Click cart button

    checkout = CheckoutPage(driver)
    checkout.checkout()
    checkout.fill_information("Test", "User", "12345")
    checkout.finish_checkout()

    # -------------------------
    # 5️⃣ Verify checkout success
    # -------------------------
    assert "THANK YOU FOR YOUR ORDER" in checkout.get_confirmation_message().upper()

    # -------------------------
    # 6️⃣ Logout
    # -------------------------
    header = HeaderPage(driver)
    header.logout()

