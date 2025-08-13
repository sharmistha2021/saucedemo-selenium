
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Cart page URL (optional, can navigate directly)
        self.url = "https://www.saucedemo.com/cart.html"
        
        # Locators
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.remove_buttons = (By.CSS_SELECTOR, ".cart_button")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_quantity_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def go_to(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def get_cart_items_count(self):
        # Returns number of items currently in the cart
        items = self.driver.find_elements(*self.cart_items)
        return len(items)

    def remove_item_by_name(self, product_name):
        items = self.driver.find_elements(*self.cart_items)
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                remove_button = item.find_element(By.CSS_SELECTOR, ".cart_button")
                remove_button.click()
                # Wait until the item is removed from the DOM
                WebDriverWait(self.driver, 10).until(EC.staleness_of(item))
                return True
        return False  # Item not found

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def get_cart_badge_count(self):
        # Returns number shown in the cart icon badge (number of items)
        try:
            badge = self.driver.find_element(*self.cart_quantity_badge)
            return int(badge.text)
        except:
            return 0  # Badge not present means cart is empty
