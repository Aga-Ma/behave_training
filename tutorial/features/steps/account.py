from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_element(browser, **locator):
    return browser.find_element(**locator)


def find_elements(browser, id):
    return browser.find_elements(By.ID, id)


@given('I search for a valid account')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000/index')
    form = get_element(context.browser, tag='form')
    get_element(form, name='msisdn').send_keys('61415551234')
    form.submit()


@then('I will see the account details')
def step_impl(context):
    # step function names do not need to have a unique symbol name it uses "step_impl" by default
    elements = find_elements(context.browser, id='no-account')
    eq_(elements, [], 'account not found')
    h = get_element(context.browser, id='account-head')
    ok_(h.text.startwith("Account '61415551234'"), 'Heading %r has wrong text' % h.text)