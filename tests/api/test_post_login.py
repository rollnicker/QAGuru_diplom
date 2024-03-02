import os

import allure
import requests
from dotenv import load_dotenv
from jsonschema import validate

from utils.logging import post_litress
from utils.open_schemas import load_schema

load_dotenv()
login: str = os.getenv("USER_LOGIN")
password: str = os.getenv("USER_PASSWORD")

AUTH_URL = "/auth/login"
LOGIN_AVAILABLE_URL = "/auth/login-available"
wrong_login = "superverymega228kek@mail.ru"
wrong_password = '123qwe'


@allure.title("Проверка авторизации")
def test_succesfull_autorisation():
    response = post_litress(AUTH_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": login, "password": password})
    body = response.json()
    validate(body,
             schema=load_schema("login_schema.json"))
    assert response.status_code == 200


@allure.title("Авторизация с неправильными данными")
def test_unsuccesfull_autorisation():
    response = post_litress(AUTH_URL,
                            headers={"Content-Type": "application/json"},
                            json={"login": wrong_login, "password": wrong_password})
    assert response.status_code == 401


@allure.title("Проверка что логин не доступен для регистрации")
def test_not_available_login_for_registration():
    response = requests.post(LOGIN_AVAILABLE_URL,
                             headers={"Content-Type": "application/json"},
                             json={"login": login})
    assert not (response.json()['payload']['data']['available'])


@allure.title("Проверка что логин доступен для регистрации")
def test_available_login_for_registration():
    response = requests.post(LOGIN_AVAILABLE_URL,
                             headers={"Content-Type": "application/json"},
                             json={"login": wrong_login})
    body = response.json()
    validate(body,
             schema=load_schema("login_available_schema.json"))
    assert (response.json()['payload']['data']['available'])
