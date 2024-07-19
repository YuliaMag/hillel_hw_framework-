import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pas_reset_page import ResetPassword
from helpers.user import User


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page_fx(browser):
    return LoginPage(browser)


@pytest.fixture
def dashboard_page_fx(browser):
    return DashboardPage(browser)


@pytest.fixture
def pas_reset_page_fx(browser):
    return ResetPassword(browser)


@pytest.fixture(scope="session")
def valid_user():
    return User("Admin", "admin123")


@pytest.fixture(scope="session")
def invalid_user():
    return User("Admin", "wrongpass###")
