from pages.main_page import MainPage
import allure 

class TestAcademy:

    @allure.title('Тест на открытие главной страницы сайта')
    def test_check_home_page_load(self, browser):
        academy_home_page = MainPage(browser)
        academy_home_page.open_browser()
        home_page = academy_home_page.chech_home_page_load()
        assert home_page, 'Home page did not load'

    @allure.title('Тест на работоспособность кнопки "Войти"')
    def test_click_button_entance(self, browser):
        academy_home_page = MainPage(browser)
        academy_home_page.open_browser()
        academy_home_page.click_button_entance()
        list_succes = academy_home_page.check_list_entance()
        assert list_succes, 'Не открылось модальное окно авторизации'

    @allure.title('Тест на ввод значения в поле email')
    def test_input_field_email(self, browser):
        academy_home_page = MainPage(browser)
        academy_home_page.open_browser()
        academy_home_page.click_button_entance()
        academy_home_page.input_field_email()
        field = academy_home_page.check_field_email()
        assert field, 'Не ввелся email пользователя'

    @allure.title('Тест на ввод значения в поле password')
    def test_input_field_password(self, browser):
        academy_home_page = MainPage(browser)
        academy_home_page.open_browser()
        academy_home_page.click_button_entance()
        academy_home_page.input_field_email()
        academy_home_page.input_field_password()
        field = academy_home_page.check_field_password()
        assert field, 'Не ввелся password пользователя'

    @allure.title('Тест на авторизацию с валидными данными пользователя')
    def test_click_button_authorization(self, browser):
        academy_home_page = MainPage(browser)
        academy_home_page.open_browser()
        academy_home_page.click_button_entance()
        academy_home_page.input_field_email()
        academy_home_page.input_field_password()
        academy_home_page.click_button_authorization()
        succes_authorization = academy_home_page.check_succes_authorization()
        assert succes_authorization, 'Пользователю не удалось авторизоваться'
