from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_locators import TestLocators
from helpers import DataHelper
from tests.conftest import driver


class TestRegistration:

    def test_registration(self, driver):
        name = DataHelper.get_name()
        email = DataHelper.get_email()
        password = DataHelper.get_password()

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_TO_AUTH).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REG).send_keys(name)
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REG).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REG).send_keys(password)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REG))
        driver.find_element(*TestLocators.BUTTON_REG).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.INPUT_EMAIL_FOR_ENTR))

        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_ENTR).send_keys(email)

        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_ENTR).send_keys(password)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTR))
        driver.find_element(*TestLocators.BUTTON_ENTR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LK))
        driver.find_element(*TestLocators.BUTTON_LK).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.LK_NAME))
        actual_name = driver.find_element(*TestLocators.LK_NAME).get_attribute('value')

        assert name == actual_name
        assert email.__contains__('@')
        assert password / 100000 > 1

    def test_registration_uncorrect_password(self, driver):
        name = DataHelper.get_name()
        email = DataHelper.get_email()
        password = DataHelper.get_uncorrect_password()

        driver.find_element(*TestLocators.BUTTON_ENTRY_INTO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_TO_AUTH).click()
        driver.find_element(*TestLocators.INPUT_NAME_FOR_REG).send_keys(name)
        driver.find_element(*TestLocators.INPUT_EMAIL_FOR_REG).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_FOR_REG).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_REG).click()

        element = driver.find_element()

        assert element is not None

