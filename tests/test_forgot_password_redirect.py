from pages.pas_reset_page import ResetPassword
from pages.login_page import LoginPage


def test_forgot_password_redirect(browser):
    login_page = LoginPage(browser)
    forgot_password_page = ResetPassword(browser)

    login_page.open()
    login_page.forgot_pas_click()

    reset_displayed = forgot_password_page.passreset_page_display()

    assert reset_displayed, ""
