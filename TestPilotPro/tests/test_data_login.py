import pytest
from pages.login_page import LoginPage
from utils.read_data import get_login_data
from utils.logger import setup_logger
from utils.popup_handler import dismiss_password_popup
import time

logger = setup_logger()

# Define valid users that should successfully log in
VALID_USERS = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]

@pytest.mark.parametrize("username,password", get_login_data())
def test_data_driven_login(driver, username, password):
    driver.get("https://www.saucedemo.com")
    
    login = LoginPage(driver)
    
    login.enter_username(username)
    logger.info(f"Username entered: {username}")
    
    login.enter_password(password)
    logger.info(f"Password entered")
    
    login.click_login()
    logger.info("Login clicked")
    
    # Handle any popup
    time.sleep(0.5)
    dismiss_password_popup(driver)
    
    # Check if login was successful based on user type
    if username in VALID_USERS:
        # For valid users, wait for inventory page
        time.sleep(1)
        assert "inventory" in driver.current_url, f"Expected inventory page for {username}, got {driver.current_url}"
        logger.info(f"Valid login success for {username}")
    else:
        # For invalid users, check for error message
        time.sleep(1)
        error_message = login.get_error_message()
        
        # If no error message, check if we're still on login page
        if error_message:
            assert "Epic sadface" in error_message, f"Expected error message for {username}, got: {error_message}"
            logger.info(f"Error message displayed correctly for {username}")
        else:
            # If no error message, we should still be on login page (not inventory)
            assert "inventory" not in driver.current_url, f"Expected to stay on login page for {username}, but redirected to inventory"
            logger.info(f"Stayed on login page as expected for {username}")