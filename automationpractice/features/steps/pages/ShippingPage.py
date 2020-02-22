from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ShippingAddressPage(BasePage):

    def __init__(self, context):
        super().__init__(
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "page_heading": (By.CLASS_NAME, "page-heading"),
        "terms": (By.ID, "cgv"),
        "proceed_to_checkout": (By.NAME, "processCarrier")
    }
