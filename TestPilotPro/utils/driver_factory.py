from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from config import BROWSER

def get_driver():

    if BROWSER == "chrome":

        options = webdriver.ChromeOptions()

        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif BROWSER == "firefox":

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    driver.maximize_window()
    return driver