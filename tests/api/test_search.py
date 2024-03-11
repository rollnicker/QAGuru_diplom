import allure
from jsonschema import validate

from litres_project.utils.logging import request_litres
from litres_project.utils.open_schemas import load_schema
from tests.api.conftest import SEARCH_URL, BASE_URL


@allure.epic('Search')
@allure.tag('api', 'positive')
@allure.title("Проверка поиска книги")
def test_check_search_book():
    book_title = 'мастер и маргарита'
    params = {"q": book_title}
    response = request_litres(base_url=BASE_URL,
                              method='GET',
                              url=SEARCH_URL,
                              params=params,
                              headers={"Content-Type": "application/json"}
                              )
    body = response.json()
    validate(body,
             schema=load_schema("search_schema.json"))
    assert response.status_code == 200
    assert book_title in (body['payload']['data'][0]['text'])


@allure.epic('Search')
@allure.tag('api', 'negative')
@allure.title("Поиск книги по неправильному названию")
def test_check_invalid_search():
    wrong_title = 'qwdcvfbetbevsef'
    params = {"q": wrong_title}
    response = request_litres(base_url=BASE_URL,
                              method='GET',
                              url=SEARCH_URL,
                              params=params,
                              headers={"Content-Type": "application/json"})
    body = response.json()
    validate(body,
             schema=load_schema("search_schema.json"))
    assert response.status_code == 200
    assert wrong_title not in (body['payload']['data'])
