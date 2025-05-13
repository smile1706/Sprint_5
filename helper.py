from faker import Faker
from locators import Locators
from data import Credentials
from conftest import driver

fake = Faker()

def generate_registration_data():
    username = fake.name()
    email = fake.email()
    correct_password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return username, email, correct_password  # Возвращаем кортеж (email, correct_password)

def generate_incorrect_registration_data():
    username = fake.name()
    email = fake.email()
    incorrect_password = fake.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return username, email, incorrect_password  # Возвращаем кортеж (email, correct_password)

def login(driver):
    driver.find_element(*Locators.EMAIL_field).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_field).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON_AT_LOGIN_PAGE).click()

    return driver
