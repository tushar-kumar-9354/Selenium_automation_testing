from selenium.webdriver.common.by import By

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
        self.driver.find_element(*self.cart_icon).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def fill_details(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    def finish_order(self):
        self.driver.find_element(*self.finish_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text