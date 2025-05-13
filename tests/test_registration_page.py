from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data, generate_incorrect_registration_data
from locators import Locators
from curl import *
from conftest import driver

class TestRegistrationWithNewCredentials:

    def test_success_registration(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        driver.find_element(*Locators.REGISTRATION_BUTTON_AT_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        username, email, correct_password = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(username)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(correct_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REDIRECT_TO_LOGIN))
        assert driver.current_url == main_site + 'login'

    def test_registration_password_error(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        driver.find_element(*Locators.REGISTRATION_BUTTON_AT_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        username, email, incorrect_password = generate_incorrect_registration_data()
        driver.find_element(*Locators.NAME).send_keys(username)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(incorrect_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        incorrect_password_error = driver.find_element(*Locators.PASSWORD_ERROR).text
        assert incorrect_password_error == 'Некорректный пароль'
