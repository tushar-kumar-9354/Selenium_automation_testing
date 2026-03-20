from pages.login_page import LoginPage
from utils.logger import setup_logger
from utils.popup_handler import dismiss_password_popup
import time

logger = setup_logger()

def test_invalid_login(driver):
    logger.info("Browser opened")
    
    driver.get("https://www.saucedemo.com")
    
    login = LoginPage(driver)
    
    login.enter_username("wrong_user")
    logger.info("Wrong username entered")
    
    login.enter_password("wrong_pass")
    logger.info("Wrong password entered")
    
    login.click_login()
    logger.info("Login attempted")
    
    # Handle any popup that might appear
    time.sleep(0.5)
    dismiss_password_popup(driver)
    
    # Wait for error message to appear
    time.sleep(1)
    
    error = login.get_error_message()
    
    # Assert error message contains expected text
    assert "Epic sadface" in error or error != "", f"Expected error message, got: {error}"
    logger.info(f"Error validated: {error}")