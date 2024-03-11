import os

import allure
from dotenv import load_dotenv

from litres_project import utils
from litres_project.web.application import app

load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
login: str = os.getenv("USER_LOGIN")
password: str = os.getenv("USER_PASSWORD")

wrong_login = "superverymega228kek@mail.ru"
bad_login = '1qazsxwsdc'
wrong_password = '123qwe'


class TestLogin:
    @allure.epic('Login')
    @allure.tag('web', 'positive')
    @allure.title('Успешная авторизация')
    def test_successful_login(self):
        app.open_page()

        app.header_panel.click_login_button()

        app.login_window.fill_login_and_password(email=login, password=password)

        app.header_panel.click_profile_button()

        app.profile_page.avatar_should_have_name('Борис Рольник')

    @allure.epic('Login')
    @allure.tag('web', 'negative')
    @allure.title('Неуспешная авторизация: неправильный пароль')
    def test_login_with_wrong_password(self):
        app.open_page()

        app.header_panel.click_login_button()

        app.login_window.fill_login_and_password(email=login, password=wrong_password)

        app.login_window.check_wrong_password_message()

    @allure.epic('Login')
    @allure.tag('web', 'negative')
    @allure.title('Неуспешная авторизация: email доступен для регистрации')
    def test_login_is_available_for_registration(self):
        app.open_page()

        app.header_panel.click_login_button()

        app.login_window.fill_login(email=wrong_login)

        app.login_window.check_free_email_message()

    @allure.epic('Login')
    @allure.tag('web', 'negative')
    @allure.title('Неуспешная авторизация: логин не найден')
    def test_bad_login(self):
        app.open_page()

        app.header_panel.click_login_button()

        app.login_window.fill_login(email=bad_login)

        app.login_window.check_bad_login_message()
