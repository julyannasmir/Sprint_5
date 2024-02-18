from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class TestsConstructor:
    def test_go_to_the_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        section = driver.find_element(*Locators.BUNS_SECTION_INDICATOR).get_attribute('class')
        assert Constants.CURRENT_SECTION in section

    def test_go_to_the_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        section = driver.find_element(*Locators.SAUCES_SECTION_INDICATOR).get_attribute('class')
        assert Constants.CURRENT_SECTION in section

    def test_go_to_the_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        section = driver.find_element(*Locators.FILLINGS_SECTION_INDICATOR).get_attribute('class')
        assert Constants.CURRENT_SECTION in section
