from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from test_locators import TestLocators
from tests.conftest import driver


class TestExitFromLk:
    def test_go_from_LK_to_constructor(self, driver):

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LK))
        driver.find_element(*TestLocators.BUTTON_LK).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT))
        driver.find_element(*TestLocators.BUTTON_EXIT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTR))
        element = driver.find_element(*TestLocators.BUTTON_ENTR)
        assert element is not None
