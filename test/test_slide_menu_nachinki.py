import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestClickTabNachinki:
    def test_slide_menu_nachinki(self, driver):

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TAB_SOUS)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TAB_BULKI)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TAB_NACHINKA)).click()
        assert driver.find_element(*Locators.VALIDATION_NACHINKI).text == 'Начинки'
