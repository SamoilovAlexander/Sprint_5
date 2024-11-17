from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestLocators import TestLocators
from tests.conftest import driver


class TestTransitionToConstructorsUnits:
    def test_transition_to_unit_stuffings(self, driver):
        email = "qa_15@gmail.com"
        password = "1234567890"

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.UNIT_STUFFINGS))
        driver.find_element(*TestLocators.UNIT_STUFFINGS).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.STUFFINGS_IN_LIST))
        stuffings = driver.find_element(*TestLocators.STUFFINGS_IN_LIST)
        assert stuffings is not None

    def test_transition_to_unit_sauces(self, driver):
        email = "qa_15@gmail.com"
        password = "1234567890"

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.UNIT_STUFFINGS))
        driver.find_element(*TestLocators.UNIT_STUFFINGS).click()
        driver.find_element(*TestLocators.UNIT_SAUCES).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.SAUCES_IN_LIST))
        stuffings = driver.find_element(*TestLocators.SAUCES_IN_LIST)
        assert stuffings.is_displayed() is True

    def test_transition_to_unit_buns(self, driver):
        email = "qa_15@gmail.com"
        password = "1234567890"

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_ENTR).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.UNIT_STUFFINGS))
        driver.find_element(*TestLocators.UNIT_STUFFINGS).click()
        driver.find_element(*TestLocators.UNIT_BUNS).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BUNS_IN_LIST))
        stuffings = driver.find_element(*TestLocators.BUNS_IN_LIST)
        assert stuffings.is_displayed() is True