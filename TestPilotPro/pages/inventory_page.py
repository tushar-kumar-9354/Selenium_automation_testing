from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_helper import wait_for_element
from config import TIMEOUT


class InventoryPage:

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    remove_button = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        wait_for_element(self.driver, self.add_to_cart_button).click()
        # Wait for the remove button to appear, confirming the product was added
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.remove_button)
        )

    def get_cart_count(self):
        # Wait for cart badge to be present, not just visible
        badge = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(self.cart_badge)
        )
        return badge.text