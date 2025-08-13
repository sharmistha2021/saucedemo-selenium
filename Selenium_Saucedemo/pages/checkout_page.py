from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/checkout-step-one.html")
        )

    def fill_information(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_button).click()
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/checkout-step-two.html")
        )

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.complete_header)
        )
        return self.driver.find_element(*self.complete_header).text
