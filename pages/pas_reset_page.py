from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResetPassword(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.open("/web/index.php/auth/requestPasswordResetCode")

    RESET_PASSWORD_FORM = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')
    USERNAME_INPUT = (By.NAME, "username")
    CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
    RESET_LINK_SENT = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')

    def passreset_page_display(self):
        reset_password = self.find_element(self.RESET_PASSWORD_FORM)
        return reset_password.is_displayed()

    def enter_username(self, user):
        self.find_element(self.USERNAME_INPUT).send_keys(user.username)

    def click_cancel_button(self):
        self.find_element(self.CANCEL_BUTTON).click()

    def click_reset_password_button(self):
        self.find_element(self.RESET_PASSWORD_BUTTON).click()

    def link_sent_successfully_displayed(self):
        link_sent_successfully = self.find_element(self.RESET_LINK_SENT)
        link_sent_successfully.is_displayed()

