import pytest
from selenium import webdriver

from data import TestData


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(TestData.URL)
    yield driver
    driver.quit()

