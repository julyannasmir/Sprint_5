from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLogout:
    def test_logout(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        current_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_INDICATOR)).text
        assert current_page == 'Вход'