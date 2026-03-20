from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()

def test_valid_login(driver):

    logger.info("Browser opened")

    driver.get("https://www.saucedemo.com")
    logger.info("Website opened")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    logger.info("Username entered")

    login.enter_password("secret_sauce")
    logger.info("Password entered")

    login.click_login()
    logger.info("Login clicked")

    assert "inventory" in driver.current_url
    logger.info("Login successful")