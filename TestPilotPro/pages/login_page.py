from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_helper import wait_for_element
from utils.popup_handler import dismiss_password_popup
from config import TIMEOUT

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
        # Click login button
        wait_for_element(self.driver, self.login_button).click()
        
        # Handle popup immediately after login
        dismiss_password_popup(self.driver)
        
        # Wait a moment for page to load or error to appear
        import time
        time.sleep(1)
        
        # Handle popup again if it appears
        dismiss_password_popup(self.driver)

    def get_error_message(self):
        """Get error message with better handling"""
        try:
            # Wait for error message to be present
            error_element = WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located(self.error_message)
            )
            # Also handle popup that might be covering it
            dismiss_password_popup(self.driver)
            return error_element.text
        except:
            # If no error message found, return empty string
            return ""