from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[''2]/form/div[4]/p')
    ERROR_MSG = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')

    def __init__(self, driver):
        super().__init__(driver)
        self.open("/web/index.php/auth/login")

    def login(self, user):
        self.find_element(self.USERNAME).send_keys(user.username)
        self.find_element(self.PASSWORD).send_keys(user.password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.ERROR_MSG

    def forgot_pas_click(self):
        self.find_element(self.FORGOT_PASSWORD_BUTTON).click()



