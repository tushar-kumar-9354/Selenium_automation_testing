from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import setup_logger
from utils.popup_handler import dismiss_password_popup
import time

logger = setup_logger()

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com")
    
    login = LoginPage(driver)
    
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    
    # Additional popup handling after login
    time.sleep(0.5)
    dismiss_password_popup(driver)
    
    logger.info("Login successful")
    
    inventory = InventoryPage(driver)
    
    # Wait a moment for inventory page to be fully loaded
    time.sleep(1)
    
    inventory.add_product()
    logger.info("Product added to cart")
    
    count = inventory.get_cart_count()
    
    assert count == "1"
    logger.info("Cart count verified")