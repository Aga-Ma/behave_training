from selenium import webdriver


def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature")


def before_scenario(context, scenario):
    print("Before scenario")
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    print("Before scenario")


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    context.browser.quit()


def after_feature(context, feature):
    print("After Feature")


def after_all(context):
    print("Executing after all")
