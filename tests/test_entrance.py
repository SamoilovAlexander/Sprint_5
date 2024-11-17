from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from test_locators import TestLocators
from tests.conftest import driver


class TestEntrance:

    def test_entrance_by_button_entrance_into_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER) is not None

    def test_entrance_by_button_user_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_LK).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        element = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER)
        assert element is not None

    def test_entrance_by_registration_form(self, driver):

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_TO_AUTH).click()
        driver.find_element(*TestLocators.LINK_TO_ENTR_IN_DIFFERENT_FORM).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        element = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER)
        assert element is not None

    def test_entrance_by_button_in_recover_password_form(self, driver):

        driver.find_element(*TestLocators.BUTTON_LK).click()
        driver.find_element(*TestLocators.LINK_TO_RECOVER_PASSWORD_FORM).click()
        driver.find_element(*TestLocators.LINK_TO_ENTR_IN_DIFFERENT_FORM).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_MAKE_AN_ORDER))
        element = driver.find_element(*TestLocators.BUTTON_MAKE_AN_ORDER)
        assert element is not None
