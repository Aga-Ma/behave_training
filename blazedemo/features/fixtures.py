from selenium import webdriver
from behave.fixture import fixture
from web.web import Web


@fixture
def browser_chrome(context):
    browser = webdriver.Chrome("C:/drivers/chromedriver.exe")
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()
