from selenium.webdriver.common.by import By

from .BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, context):
        super().__init__(
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "unit_price": (By.CLASS_NAME, "special-price"),
        "total_price": (By.ID, "total_price"),
        "proceed_to_checkout": (By.LINK_TEXT, "Proceed to checkout")
    }