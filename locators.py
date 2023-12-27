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

    '''Тестирование Табов Конструктора'''
    TAB_BULKI = (By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(1) > span")
    TAB_SOUS = (By.XPATH, "//span[text()='Соусы']")
    TAB_NACHINKA = (By.XPATH, "//span[text()='Начинки']")

    VALIDATION_NACHINKI = (By.XPATH, "//h2[text()='Начинки']")
    VALIDATION_SOUS = (By.XPATH, "//h2[text()='Соусы']")
    VALIDATION_BULKI = (By.XPATH, "//h2[text()='Булки']")

    LINK = 'https://stellarburgers.nomoreparties.site/'
    LINK_PROFILE = 'https://stellarburgers.nomoreparties.site/account/profile'
    LINK_LOGIN = '/login'