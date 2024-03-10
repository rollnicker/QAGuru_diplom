import os

import allure
from allure_commons._allure import step
from dotenv import load_dotenv

from QAGuru_litres import utils
from QAGuru_litres.web.application import app

load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
login: str = os.getenv("USER_LOGIN")
password: str = os.getenv("USER_PASSWORD")

wrong_login = "superverymega228kek@mail.ru"
bad_login = '1qazsxwsdc'
wrong_password = '123qwe'


@allure.epic('Login')
@allure.tag('web', 'positive')
@allure.title('Успешный логин')
def test_successful_login(setup_browser):
    with step("Открыть форму логина"):
        app.header_panel.click_login_button()

    with step("Ввести логин и пароль"):
        app.login_window.fill_login_and_password(email=login, password=password)

    with step("проверить что авторизация успешна"):
        app.header_panel.click_profile_button()
        app.profile_page.avatar_should_have_name('Борис Рольник')


@allure.epic('Login')
@allure.tag('web', 'negative')
@allure.title('Неуспешный логин: неправильный пароль')
def test_login_with_wrong_password(setup_browser):
    with step("Открыть форму логина"):
        app.header_panel.click_login_button()

    with step("Ввести логин и пароль"):
        app.login_window.fill_login_and_password(email=login, password=wrong_password)

    with (step("проверить что появилось сообщение об ошибке")):
        app.login_window.check_wrong_password_message()


@allure.epic('Login')
@allure.tag('web', 'negative')
@allure.title('Неуспешный логин: email доступен для регистрации')
def test_login_is_available_for_registration(setup_browser):
    with step("Открыть форму логина"):
        app.header_panel.click_login_button()

    with step("Ввести логин, которого нет в системе"):
        app.login_window.fill_login(email=wrong_login)

    with (step("проверить что появилось сообщение 'данный email не зарегистрирован'")):
        app.login_window.check_free_email_message()


@allure.epic('Login')
@allure.tag('web', 'negative')
@allure.title('Неуспешный логин: логин не найден')
def test_bad_login(setup_browser):
    with step("Открыть форму логина"):
        app.header_panel.click_login_button()

    with step("Ввести логин, которого нет в системе"):
        app.login_window.fill_login(email=bad_login)

    with (step("проверить что появилось сообщение 'пользователь не найден'")):
        app.login_window.check_bad_login_message()
