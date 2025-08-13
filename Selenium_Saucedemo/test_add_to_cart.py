from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

driver = setup_driver()

try:
    # Login
    login_page = LoginPage(driver)
    login_page.go_to()
    login_page.login("standard_user", "secret_sauce")

    # Add first item to cart
    add_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item button.btn_inventory")
    add_button.click()

    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
        )
        print("✅ Add to Cart test passed")
    except TimeoutException:
        print("❌ Add to Cart test failed")

finally:
    driver.quit()
