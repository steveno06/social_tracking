import unittest
from selenium import webdriver
import page

class SocialLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://127.0.0.1:5000/")

    def test_login(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matching()
        mainPage.username_text_element = "test"
        mainPage.password_text_element = "test"
        mainPage.click_login_button()

        logged_in_page = page.LoggedInPage(self.driver)
        assert logged_in_page.is_login()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()