from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # DASHBOARD_PAGE = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]')
    DASHBOARD_PAGE = (By.TAG_NAME, 'h6') # I don't trust it

    def dashboard_displayed(self):
        dashboard = self.find_element(self.DASHBOARD_PAGE)
        return dashboard.is_displayed()
