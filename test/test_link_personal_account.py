from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLinkPersonalAccount:
    def test_link_personal_account(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR))
        personal_account_page_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_INDICATOR)).text
        assert personal_account_page_text == 'Профиль'