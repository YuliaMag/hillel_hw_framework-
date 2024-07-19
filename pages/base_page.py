from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)
        self.base_url = "https://opensource-demo.orangehrmlive.com/"

    def open(self, url_path=""):
        url = self.base_url + url_path
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
