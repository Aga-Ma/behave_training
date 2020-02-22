from selenium.webdriver.common.by import By

from .BasePage import BasePage


class OrderConfirmationPage(BasePage):

    def __init__(self, context):
        super().__init__(
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "page_heading": (By.CLASS_NAME, "page-heading"),
        "confirm_alert": (By.CLASS_NAME, "alert-success")
    }
