# tests/test_login_flipkart.py

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from base.base_test import setup
from utilities.screenshots import Screenshots


@pytest.mark.usefixtures("setup")
class TestFlipkart:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.main_window = None
        self.login_page = LoginPage(self.driver)

    def test_login_search_add_cart(self):
        """
        Test flow:
        1. Open Flipkart
        2. Login
        3. Search for Samsung Flat TV
        4. Add first product to cart
        """
        self.driver.get("https://www.flipkart.com/")
        self.main_window = self.driver.current_window_handle

        # Logging
        print("➡️ Opened Flipkart homepage")
        self.login_page.close_login_popup()

        # Login steps
        self.login_page.click_login_link()
        self.login_page.enter_mobile_number("9042016644")  # Replace with your number
        self.login_page.click_request_otp()
        print("⚠️ Please enter OTP manually in browser...")

        # Wait for login to complete manually
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1ruvv2")))
            print("✅ Login successful")
        except Exception:
            print("❌ Login not completed")

        # Search for product
        self.search_product("Samsung Flat TV")

        # Add first product to cart
        self.click_first_product_add_to_cart()
        print("✅ First Samsung Flat TV added to cart successfully")

    def search_product(self, query):
        search_box = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@title='Search for Products, Brands and More']"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='/p/']")))
        print(f"🔍 Search for '{query}' completed")

    def click_first_product_add_to_cart(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/p/']"))
        )
        product = products[0]
        self.actions.move_to_element(product).perform()
        first_product_link = product.get_attribute("href")

        # Open product in new tab
        self.driver.execute_script("window.open(arguments[0], '_blank');", first_product_link)
        self.switch_to_new_tab()

        # Click Add to Cart
        add_to_cart = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add to cart') or contains(.,'ADD TO CART')]"))
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart)
        time.sleep(2)

        # Close tab and switch back
        self.driver.close()
        self.driver.switch_to.window(self.main_window)

    def switch_to_new_tab(self):
        for handle in self.driver.window_handles:
            if handle != self.main_window:
                self.driver.switch_to.window(handle)
                break
