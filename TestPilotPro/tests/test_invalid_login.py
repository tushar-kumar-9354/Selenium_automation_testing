from pages.login_page import LoginPage
from utils.logger import setup_logger

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

    error = login.get_error_message()

    assert "Epic sadface" in error
    logger.info("Error validated")