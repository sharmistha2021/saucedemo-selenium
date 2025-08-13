from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def test_valid_login():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert "inventory" in driver.current_url
        print("✅ Valid Login Test Passed")
    except Exception as e:
        print(f"❌ Valid Login Test Failed: {e}")
    finally:
        driver.quit()

def test_invalid_login():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        error_text = error_element.text
        assert "Epic sadface: Username and password do not match any user in this service" in error_text
        print("✅ Invalid Login Test Passed")
    except Exception as e:
        print(f"❌ Invalid Login Test Failed: {e}")
    finally:
        driver.quit()


def test_invalid_username_login():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        error_text = error_element.text
        assert "Epic sadface: Username and password do not match any user in this service" in error_text
        print("✅ Invalid Password Login Test Passed")
    except Exception as e:
        print(f"❌ Invalid Password Login Test Failed: {e}")
    finally:
        driver.quit()

def test_invalid_password_login():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        error_text = error_element.text
        assert "Epic sadface: Username and password do not match any user in this service" in error_text
        print("✅ Invalid username Login Test Passed")
    except Exception as e:
        print(f"❌ Invalid username Login Test Failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_invalid_password_login()
    test_invalid_username_login()
