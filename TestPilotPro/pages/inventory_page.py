from selenium.webdriver.common.by import By
from utils.wait_helper import wait_for_element


class InventoryPage:

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        wait_for_element(self.driver, self.add_to_cart_button).click()

    def get_cart_count(self):
        return wait_for_element(self.driver, self.cart_badge).text