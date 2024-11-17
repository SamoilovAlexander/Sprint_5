from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from test_locators import TestLocators
from tests.conftest import driver


class TestGoToPersonalAccount:
    def test_go_to_personal_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTR))
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LK))
        driver.find_element(*TestLocators.BUTTON_LK).click()

        assert TestData.EMAIL == driver.find_element(*TestLocators.LK_EMAIL).get_attribute('value')
