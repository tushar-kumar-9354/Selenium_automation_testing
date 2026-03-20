from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT

def wait_for_element(driver, locator):
    return WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )