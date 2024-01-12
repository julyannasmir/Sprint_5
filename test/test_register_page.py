from faker import Faker
from faker.generator import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

faker = Faker()


class TestsRegisterPage:
    def test_registration(self, driver):
        name = 'jul'
        email = faker.email()
        password = random.randint(100000, 99999999)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTER_PAGE_INDICATOR))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        current_email = driver.find_element(*Locators.PROFILE_EMAIL).get_attribute('value')
        assert current_email == email

    def test_registration_with_password_less_six_symbols(self, driver):
        name = 'jul'
        email = faker.email()
        password = random.randint(100, 99999)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        error_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD)).text
        assert error_text == 'Некорректный пароль'
