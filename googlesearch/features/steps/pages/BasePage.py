class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def visit(self, url):
        self.driver.get(url)
