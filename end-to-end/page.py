from locator import *
from element import BasePageElement

class UsernameTextElement(BasePageElement):
    locator = "username"

class PasswordTextElement(BasePageElement):
    locator = "password"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()

    def is_title_matching(self):
        return "Social Tracking" in self.driver.title
    
    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

class LoggedInPage(BasePage):
    
    def is_login(self):
        return "logout" in self.driver.page_source