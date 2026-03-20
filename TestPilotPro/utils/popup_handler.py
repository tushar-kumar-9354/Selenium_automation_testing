from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def dismiss_password_popup(driver):
    """Force dismiss Chrome password breach popup using multiple methods"""
    
    # Give the popup a moment to appear
    time.sleep(0.5)
    
    # Method 1: Press Escape key multiple times
    try:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(0.2)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(0.2)
    except:
        pass
    
    # Method 2: Try to find and click any OK button
    try:
        ok_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'OK')]")
        for button in ok_buttons:
            if button.is_displayed():
                button.click()
                time.sleep(0.2)
                break
    except:
        pass
    
    # Method 3: Click outside the popup (click at coordinates 0,0)
    try:
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(driver)
        actions.move_by_offset(0, 0).click().perform()
        actions.reset_actions()
    except:
        pass

def handle_password_breach_popup(driver):
    """Alias for dismiss_password_popup for backward compatibility"""
    dismiss_password_popup(driver)