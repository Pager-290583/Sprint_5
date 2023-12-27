from selenium.webdriver.common.by import By


class TestClickAllKonstsruktor:
    def test_slide_menu_sous(self, driver):
        driver.find_element(By.XPATH, "//span[contains(.,'Начинки')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Булки')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Соусы')]").click()
        assert driver.find_element(By.XPATH, "//span[contains(.,'Соусы')]").text == 'Соусы'
