from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *
from conftest import driver
from helper import login


class TestRedirectMainPageToAccountPage: #Переход в личный кабинет по клику на «Личный кабинет»

    def test_account_button_redirects_to_profile_page(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        assert driver.current_url == account_page_url


class TestRedirectAccountPageToConstructor: #Переход из личного кабинета в конструктор

    def test_click_on_constructor_redirects_to_main_page(self,driver): #по клику на «Конструктор»
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site

    def test_click_on_logo_redirects_to_main_page(self,driver): #по клику на логотип Stellar Burgers
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site


class TestLogoutButton: #Выход из аккаунта по кнопке «Выйти» в личном кабинете

    def test_logout_button_logs_out(self,driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_AT_LOGIN_PAGE))
        assert driver.current_url == login_page_url


class TestNavigateConstructorSections: #проверка переходов к разделам конструктора

    def test_click_buns_section_shows_buns_elements(self,driver): #«Булки»
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.SAUCES).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_SAUCES_TAB))
        driver.find_element(*Locators.BUNS).click()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_BUNS_TAB))
        assert "Булки" in active_tab.text

    def test_click_sauces_section_shows_sauces_elements(self,driver): #«Соусы»
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.SAUCES).click()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_SAUCES_TAB))
        assert "Соусы" in active_tab.text

    def test_click_fillings_section_shows_fillings_elements(self,driver): #«Начинки»
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators.OVERLAY))
        driver.find_element(*Locators.FILLINGS).click()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_FILLINGS_TAB))
        assert "Начинки" in active_tab.text
