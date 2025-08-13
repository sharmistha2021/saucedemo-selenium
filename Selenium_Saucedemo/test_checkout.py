from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

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

    # Add item to cart
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button.btn_inventory").click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
    )

    # Go to cart
    cart_page = CartPage(driver)
    cart_page.go_to()

    # Start checkout process
    checkout_page = CheckoutPage(driver)
    checkout_page.start_checkout() 
    checkout_page.fill_information("Sharmistha", "Sarkar", "1234")
    confirmation_text = checkout_page.finish_checkout()

    if "Thank you for your order!" in confirmation_text:
        print("✅ Checkout test passed")
    else:
        print("❌ Checkout test failed")

finally:
    driver.quit()
