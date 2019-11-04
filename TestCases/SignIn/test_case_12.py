import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignInTest12(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_12(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on hamburger icon
        signin.click_hamburger_icon()
        # Click on "Having trouble signing in" link
        signin.click_hamburger_icon_2()
        time.sleep(1)
        # Verify if the form changed to "Forgot your password?"
        element = self.driver.find_element_by_xpath(SignIn.verify_forgot_pass)
        assert element.is_displayed()
        # Click back arrow (next to "Booking.com Account")
        signin.click_back_arrow()
        time.sleep(1)
        # Verify if the form changed to "Sign in"
        element = self.driver.find_element_by_xpath(SignIn.verify_signin)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest12"))