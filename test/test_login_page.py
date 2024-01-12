from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class TestsLoginPage:
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        current_email = driver.find_element(*Locators.PROFILE_EMAIL).get_attribute('value')
        assert current_email == Constants.TEST_EMAIL

    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        current_email = driver.find_element(*Locators.PROFILE_EMAIL).get_attribute('value')
        assert current_email == Constants.TEST_EMAIL

    def test_login_from_registration_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTER_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_LINK_FROM_REGISTER_PAGE).click()
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        current_email = driver.find_element(*Locators.PROFILE_EMAIL).get_attribute('value')
        assert current_email == Constants.TEST_EMAIL

    def test_login_from_restore_password_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.RESTORE_PASSWORD_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.RESTORE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAVE_NEW_PASSWORD_BUTTON))
        driver.find_element(*Locators.SIGH_IN_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR))
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        current_email = driver.find_element(*Locators.PROFILE_EMAIL).get_attribute('value')
        assert current_email == Constants.TEST_EMAIL