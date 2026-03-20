from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from config import BROWSER

def get_driver():

    if BROWSER == "chrome":
        options = webdriver.ChromeOptions()

        # Disable ALL password-related features
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "profile.password_manager_leak_detection": False,
            "safebrowsing.enabled": False,
            "safebrowsing.disable_download_protection": True,
        })

        # Disable all security and password features via command line
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordImport")
        options.add_argument("--disable-features=PasswordCheck")
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-features=PasswordManagerOnboarding")
        options.add_argument("--disable-features=PasswordProtectionService")
        options.add_argument("--disable-features=PasswordManager")
        options.add_argument("--disable-features=PasswordManagerAllowShowPasswords")
        options.add_argument("--disable-features=PasswordManagerFillOnAccountSelect")
        
        # Run in incognito mode to avoid any saved passwords
        options.add_argument("--incognito")
        
        # Additional arguments to suppress popups
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-extensions")
        
        # Run headless if needed (uncomment if you want headless)
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif BROWSER == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.disable_beforeunload", True)
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("signon.autofillForms", False)
        options.set_preference("browser.safebrowsing.enabled", False)
        options.set_preference("security.insecure_field_warning.contextual.enabled", False)
        options.set_preference("security.certerrors.mitm.auto_enable_enterprise_roots", False)
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    driver.maximize_window()
    return driver