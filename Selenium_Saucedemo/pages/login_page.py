from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def go_to(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.error_message))
        return element.text
