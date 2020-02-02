# Python step implementation for the scenarios
# https://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations

from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False
    
@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False