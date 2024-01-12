from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsLinkConstructor:
    def test_link_from_personal_account_to_constructor(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        main_page_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR)).text
        assert main_page_text == "Соберите бургер"

    def test_link_from_personal_account_to_stellar_burger(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        driver.find_element(*Locators.STELLAR_BURGER_BUTTON).click()
        main_page_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_INDICATOR)).text
        assert main_page_text == "Соберите бургер"