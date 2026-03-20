from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT

class CheckoutPage:

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    checkout_button = (By.ID, "checkout")

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")

    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    success_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        # Wait for cart icon to be clickable
        cart = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        cart.click()
        
        # Wait for cart page to load
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.url_contains("cart.html")
        )

    def click_checkout(self):
        # Wait for checkout button to be present and clickable
        checkout_btn = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()
        
        # Wait for checkout page to load
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.url_contains("checkout-step-one")
        )

    def fill_details(self, fname, lname, zipcode):
        # Wait for first name field to be visible and interactable
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.first_name)
        )
        
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zipcode)

    def continue_checkout(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
        
        # Wait for checkout overview page
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.url_contains("checkout-step-two")
        )

    def finish_order(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
        
        # Wait for completion page
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.url_contains("checkout-complete")
        )

    def get_success_message(self):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.success_message)
        ).text