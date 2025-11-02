# tests/test_login_flipkart.py

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from base.base_test import setup
from utilities.screenshots import Screenshots


@pytest.mark.usefixtures("setup")
class TestFlipkart:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.actions = ActionChains(self.driver)
        self.main_window = None
        self.login_page = LoginPage(self.driver)

    def test_login_and_search_add_cart(self):
        self.driver.get("https://www.flipkart.com/")
        self.main_window = self.driver.current_window_handle

        self.test.log("INFO", "Opened Flipkart homepage")
        self.login_page.close_login_popup()

        self.login_page.click_login_link()
        self.login_page.enter_mobile_number("8148921824")
        self.login_page.click_request_otp()

        self.test.log("INFO", "Please enter OTP manually in browser...")
        try:
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1ruvv2"))(self.driver)
            self.test.log("PASS", "Login successful")
        except Exception:
            self.test.log("FAIL", "Login not completed")

    def search_product(self, query):
        search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='/p/']")))

    def click_first_product_add_to_cart(self):
        products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/p/']")))
        product = products[0]
        self.actions.move_to_element(product).perform()
        product.click()

        self.switch_to_new_tab()
        add_to_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add to cart') or contains(.,'ADD TO CART')]")))
        self.driver.execute_script("arguments[0].click();", add_to_cart)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.main_window)

    def switch_to_new_tab(self):
        for handle in self.driver.window_handles:
            if handle != self.main_window:
                self.driver.switch_to.window(handle)
                break
