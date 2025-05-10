from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *
from conftest import driver,login

class TestLogin:

    def test_login_from_main_page_sign_in(self,driver):
        WebDriverWait(driver,10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable (Locators.ORDER_BUTTON))
        assert driver.current_url == main_site

    def test_login_from_account_page_sign_in(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site

    def test_login_from_registration_page_sign_in(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        driver.find_element(*Locators.REGISTRATION_BUTTON_AT_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON_AT_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site

    def test_login_from_forgot_page_sign_in(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        driver.find_element(*Locators.FORGOT_BUTTON_AT_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.RECOVER_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON_AT_FORGOT_PAGE).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site
