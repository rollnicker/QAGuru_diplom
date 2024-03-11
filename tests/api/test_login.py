import allure
from jsonschema import validate

from litres_project.utils.logging import request_litres
from litres_project.utils.open_schemas import load_schema
from tests.api.conftest import login, password, AUTH_URL, wrong_login, wrong_password, LOGIN_AVAILABLE_URL, BASE_URL


@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Проверка авторизации")
def test_successful_authorization():
    response = request_litres(base_url=BASE_URL,
                              method='POST',
                              url=AUTH_URL,
                              headers={"Content-Type": "application/json"},
                              json={"login": login, "password": password})
    body = response.json()
    validate(body,
             schema=load_schema("login_schema.json"))
    assert response.status_code == 200
    assert body['error'] == None


@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Авторизация с неправильными данными")
def test_unsuccessful_authorization():
    response = request_litres(base_url=BASE_URL,
                              method='POST',
                              url=AUTH_URL,
                              headers={"Content-Type": "application/json"},
                              json={"login": wrong_login, "password": wrong_password})
    body = response.json()
    validate(body,
             schema=load_schema("bad_password.json"))
    assert response.status_code == 401
    assert response.json()['error']['title'] == 'Incorrect user data'


@allure.epic('Login')
@allure.tag('api', 'negative')
@allure.title("Проверка что логин не доступен для регистрации")
def test_not_available_login_for_registration():
    response = request_litres(base_url=BASE_URL,
                              method='POST',
                              url=LOGIN_AVAILABLE_URL,
                              headers={"Content-Type": "application/json"},
                              json={"login": login})
    body = response.json()
    validate(body,
             schema=load_schema("login_available_schema.json"))
    assert response.status_code == 200
    assert not (response.json()['payload']['data']['available'])

@allure.epic('Login')
@allure.tag('api', 'positive')
@allure.title("Проверка что логин доступен для регистрации")
def test_available_login_for_registration():
    response = request_litres(base_url=BASE_URL,
                              method='POST',
                              url=LOGIN_AVAILABLE_URL,
                              headers={"Content-Type": "application/json"},
                              json={"login": wrong_login})
    body = response.json()
    validate(body,
             schema=load_schema("login_available_schema.json"))
    assert response.status_code == 200
    assert (response.json()['payload']['data']['available'])
