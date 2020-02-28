from selenium.webdriver.common.by import By

from .BasePage import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "signin_button": (By.ID, 'SubmitLogin')
    }

    def __init__(self, context):
        super().__init__(
            context.browser,
            base_url='http://www.practiceselenium.com/')

    def login(self, username="baxome2199@kamismail.com", passwd="poiuytrewq123"):
        self.find_element(*self.locator_dictionary['email']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['signin_button']).click()
