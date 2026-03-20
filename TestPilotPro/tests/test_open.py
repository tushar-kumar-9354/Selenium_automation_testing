from utils.driver_factory import get_driver

def test_open_google():
    driver = get_driver()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()