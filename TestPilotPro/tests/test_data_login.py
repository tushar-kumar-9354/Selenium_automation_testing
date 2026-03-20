import pytest
from pages.login_page import LoginPage
from utils.read_data import get_login_data
from utils.logger import setup_logger

logger = setup_logger()

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

    if username == "standard_user":
        assert "inventory" in driver.current_url
        logger.info("Valid login success")
    else:
        assert "Epic sadface" in driver.page_source or "inventory" in driver.current_url
        logger.info("Handled other user case")