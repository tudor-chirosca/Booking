import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest34(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@djimail.com"
    password = "12345678"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_34(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter a valid email account (jacknicholson@djimail.com)
        signin.set_email(self.email)
        # Click on "Next" button
        signin.click_next_button()
        time.sleep(1)
        # Enter a valid password (12345678)
        signin.set_password(self.password)
        signin.verify_password()
        # Click "Sign in" button
        signin.click_password_signin_button()
        # Verify if an error message appears (Enter your Booking.com password)
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.alert_message_2)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest34"))
