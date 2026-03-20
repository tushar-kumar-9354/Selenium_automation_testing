from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.logger import setup_logger

logger = setup_logger()

def test_checkout_flow(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    logger.info("Login successful")

    inventory = InventoryPage(driver)
    inventory.add_product()

    logger.info("Product added")

    checkout = CheckoutPage(driver)

    checkout.open_cart()
    logger.info("Cart opened")

    checkout.click_checkout()
    logger.info("Checkout clicked")

    checkout.fill_details("Tushar", "Kumar", "110001")
    logger.info("Customer details entered")

    checkout.continue_checkout()
    logger.info("Checkout continued")

    checkout.finish_order()
    logger.info("Order finished")

    success = checkout.get_success_message()

    assert "Thank you" in success
    logger.info("Order success verified")