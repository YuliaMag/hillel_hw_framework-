from pages.login_page import LoginPage


def test_unsuccessful_login(browser, invalid_user):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.login(invalid_user)

    assert login_page.get_error_message()

