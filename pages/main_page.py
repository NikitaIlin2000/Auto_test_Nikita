from pages.base_page import *
from config.constants import *
import allure

class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Шаг на открытие главной страницы')
    def open_browser(self):
        try:
            self.open(LINK)

        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

    def chech_home_page_load(self):
        try:
            home_page = self.home_page_load(Selectors.LOCATOR_HOME_PAGE)
            return home_page

        except Exception as e:
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
             raise e
    
    @allure.step('Шаг на клик по кнопке "Войти" (для открытия модального окна "Вход")')
    def click_button_entance(self):
        try:
            button_entance = self.button_entrance(Selectors.LOCATOR_BUTTON_ENTRANCE)
            button_entance.click()
            return button_entance
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

            raise e
    
    def check_list_entance(self):
        try:
            list_entrance = self.ch_list_entance(Selectors.LOCATOR_LIST_ENTRANCE)
            return list_entrance
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step('Шаг на ввод валидного email в поле "Email"')
    def input_field_email(self):
        try:
            input_email = self.field_email(Selectors.LOCATOR_FIELD_EMAIL)
            input_email.send_keys(USERNAME)
            return input_email
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
    
    def check_field_email(self):
        try:
            check_email = self.ch_field_email(Selectors.LOCATOR_FIELD_EMAIL, USERNAME)
            return check_email
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step('Шаг на ввод валидного пароля в поле "Пароль"')
    def input_field_password(self):
        try:
            input_password = self.field_password(Selectors.LOCATOR_FIELD_PASSWORD)
            input_password.send_keys(PASSWORD)
            return input_password
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
        
    def check_field_password(self):
        try:
            check_password = self.ch_field_password(Selectors.LOCATOR_FIELD_PASSWORD, PASSWORD)
            return check_password
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e 
    
    @allure.step('Шаг на клик по кнопке "Войти" (для авторизации на сайт)')
    def click_button_authorization(self):
        try:
            button_auth = self.button_authorization(Selectors.LOCATOR_BUTTON_AUTHORIZATION)
            button_auth.click()
            return button_auth
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e 
    
    def check_succes_authorization(self):
        try:
            succes_authorization = self.ch_succes_authorization(Selectors.LOCATOR_SUCCES_AUTHORIZATION)
            return succes_authorization
        
        except Exception as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e 