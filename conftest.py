import pytest
from selenium import webdriver

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    browser.get(main_site)
    yield browser
    browser.quit()


#@pytest.fixture
def login(driver):
    # Вводим email в поле "Email"
    driver.find_element(*Locators.EMAIL_field).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_field).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON_AT_LOGIN_PAGE).click()

    return driver
