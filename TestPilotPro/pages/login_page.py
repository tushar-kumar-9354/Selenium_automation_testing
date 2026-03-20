from selenium.webdriver.common.by import By
from utils.wait_helper import wait_for_element

class LoginPage:

    username_box = (By.ID, "user-name")
    password_box = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        wait_for_element(self.driver, self.username_box).send_keys(username)

    def enter_password(self, password):
        wait_for_element(self.driver, self.password_box).send_keys(password)

    def click_login(self):
        wait_for_element(self.driver, self.login_button).click()

    def get_error_message(self):
        return wait_for_element(self.driver, self.error_message).text