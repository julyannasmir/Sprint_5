from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestsConstructor:
    def test_got_to_the_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        current_section = driver.find_element(*Locators.BUNS_SECTION_INDICATOR).get_attribute('class')
        assert current_section == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_got_to_the_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        current_section = driver.find_element(*Locators.SAUCES_SECTION_INDICATOR).get_attribute('class')
        assert current_section == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_got_to_the_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        current_section = driver.find_element(*Locators.FILLINGS_SECTION_INDICATOR).get_attribute('class')
        assert current_section == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
