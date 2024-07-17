from pages.pas_reset_page import ResetPassword
from pages.login_page import LoginPage


def test_password_reset_submit(browser, valid_user):
    login_page = LoginPage(browser)
    forgot_password_page = ResetPassword(browser)

    login_page.open()
    login_page.forgot_pas_click()

    forgot_password_page.passreset_page_display()

    forgot_password_page.enter_username(valid_user)
    forgot_password_page.click_reset_password_button()

    link_sent_successfully_displayed = forgot_password_page.link_sent_successfully_displayed

    assert link_sent_successfully_displayed, ""
