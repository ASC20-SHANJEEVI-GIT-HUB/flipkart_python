# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.close_popup = (By.XPATH, "//button[contains(@class,'_2KpZ6l _2doB4z')]")
        self.login_link = (By.XPATH, "//a[@class='_1TOQfO' and @title='Login']")
        self.mobile_field = (By.XPATH, "//input[contains(@class,'r4vIwl') and contains(@class,'BV+Dqf')]")
        self.request_otp = (By.XPATH, "//button[contains(@class,'QqFHMw') and contains(@class,'twnTnD') and contains(@class,'_7Pd1Fp')]")

    def close_login_popup(self):
        try:
            popup = self.wait.until(EC.visibility_of_element_located(self.close_popup))
            popup.click()
            print("Login popup closed.")
        except Exception:
            print("No login popup displayed.")

    def click_login_link(self):
        login = self.wait.until(EC.element_to_be_clickable(self.login_link))
        login.click()
        print("Login link clicked.")

    def enter_mobile_number(self, mobile_number):
        mobile_input = self.wait.until(EC.visibility_of_element_located(self.mobile_field))
        mobile_input.clear()
        mobile_input.send_keys(mobile_number)
        print(f"Entered mobile number: {mobile_number}")

    def click_request_otp(self):
        otp_btn = self.wait.until(EC.element_to_be_clickable(self.request_otp))
        otp_btn.click()
        print("Clicked Request OTP button.")
