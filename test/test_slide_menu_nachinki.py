from selenium.webdriver.common.by import By


class TestClickAllKonstsruktor:
    def test_slide_menu_nachinki(self, driver):
        driver.find_element(By.XPATH, "//span[contains(.,'Соусы')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Начинки')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Булки')]").click()
        assert driver.find_element(By.XPATH, "//span[contains(.,'Начинки')]").text == 'Начинки'
