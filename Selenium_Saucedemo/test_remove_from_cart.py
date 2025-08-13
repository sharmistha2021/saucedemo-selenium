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

    # Add an item so we have something to remove
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button.btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.url_contains("/cart.html"))

    # Remove the item
    remove_button = driver.find_element(By.CSS_SELECTOR, ".cart_button")
    remove_button.click()

    try:
        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        print("✅ Remove from Cart test passed")
    except TimeoutException:
        print("❌ Remove from Cart test failed")

finally:
    driver.quit()
