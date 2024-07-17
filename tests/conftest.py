import pytest
from selenium import webdriver
from pages.user import User


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def valid_user():
    return User("Admin", "admin123")


@pytest.fixture
def invalid_user():
    return User("Admin", "wrongpass###")
