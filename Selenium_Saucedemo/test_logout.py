from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

driver = setup_driver()

try:
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.go_to()
    login_page.login("standard_user", "secret_sauce")

    # Wait until inventory page is visible
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    print("✅ Login successful")

    # Step 2: Open menu (burger icon in top-left)
    menu_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()

    # Step 3: Click logout link
    logout_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()

    # Step 4: Verify logout
    WebDriverWait(driver, 5).until(
        EC.url_contains("/"),
    )
    print("✅ Logout successful")

finally:
    driver.quit()
