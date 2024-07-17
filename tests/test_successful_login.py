from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_successful_login(browser, valid_user):
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)

    login_page.open()
    login_page.login(valid_user)

    assert dashboard_page.dashboard_displayed()

