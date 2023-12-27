from selenium.webdriver.common.by import By


class Locators:
    AUTH_BUTTON = (By.XPATH, "//p[contains(.,'Личный Кабинет')]")
    REG_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    REG_BUTTON_2 = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    PASSWORD_PASS = (By.NAME, "Пароль")
    PASSWORD_FAIL = (By.NAME, "Пароль")

    ENTER_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    ENTER_BUTTON_2 = (By.XPATH, '//a[text()="Войти"]')
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    STATIC_PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    '''Index Page'''
    BUTTON_LOGIN_INDEX_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    VALIDATION_TEXT = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    BUTTON_LOGOUT = (By.XPATH, "//button[contains(.,'Выход')]")
    BUTTON_CONSTRUCTOR = (By.XPATH, "// p[contains(., 'Конструктор')]")
    BUTTON_LOGO = (By.XPATH, "//a[@class='active']")

