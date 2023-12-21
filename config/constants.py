from selenium.webdriver.common.by import By

LINK = "https://sql-academy.org/ru"

USERNAME = "nikitka.ilin.1997@mail.ru"
PASSWORD = "89038928711Qq"

class Selectors:

    LOCATOR_HOME_PAGE = (By.XPATH, '//img[@alt="Логотип sql academy"]')
    LOCATOR_BUTTON_ENTRANCE = (By.XPATH, '//div[text()="Войти"]')
    LOCATOR_LIST_ENTRANCE = (By.XPATH, '//div[text()="Вход"]')
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//input[@type="email"]')
    LOCATOR_FIELD_PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOCATOR_BUTTON_AUTHORIZATION = (By.CSS_SELECTOR, 'div.login-btn > button > div.sc-ac123477-2 > div.sc-ac123477-5')
    LOCATOR_SUCCES_AUTHORIZATION = (By.XPATH, '//img[@alt="avatar"]')