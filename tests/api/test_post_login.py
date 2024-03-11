import os

import allure
from dotenv import load_dotenv
from jsonschema import validate

from litres_project import utils
from litres_project.utils.logging import post_litress
from litres_project.utils.open_schemas import load_schema

load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
login: str = os.getenv("USER_LOGIN")
password: str = os.getenv("USER_PASSWORD")

AUTH_URL = "/auth/login"
LOGIN_AVAILABLE_URL = "/auth/login-available"
wrong_login = "superverymega228kek@mail.ru"
wrong_password = '123qwe'


@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Проверка авторизации")
def test_succesfull_autorisation():
    response = post_litress(AUTH_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": login, "password": password})
    body = response.json()
    validate(body,
             schema=load_schema("login_schema.json"))
    assert response.status_code == 200


@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Авторизация с неправильными данными")
def test_unsuccesfull_autorisation():
    response = post_litress(AUTH_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": wrong_login, "password": wrong_password})
    assert response.status_code == 401


@allure.epic('Login')
@allure.tag('api', 'negative')
@allure.title("Проверка что логин не доступен для регистрации")
def test_not_available_login_for_registration():
    response = post_litress(LOGIN_AVAILABLE_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": login})
    assert not (response.json()['payload']['data']['available'])


@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Проверка что логин доступен для регистрации")
def test_available_login_for_registration():
    response = post_litress(url=LOGIN_AVAILABLE_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": wrong_login})
    body = response.json()
    validate(body,
             schema=load_schema("login_available_schema.json"))
    assert (response.json()['payload']['data']['available'])
