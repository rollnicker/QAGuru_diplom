import allure
from jsonschema import validate

from utils.logging import get_litress
from utils.open_schemas import load_schema

@allure.title("Проверка поиска книги")
def test_check_search_book():
    book_title = 'мастер и маргарита'
    SEARCH = f'search/suggestions?q={book_title}'
    response = get_litress(url=SEARCH, headers={"Content-Type": "application/json"})
    body = response.json()
    validate(body,
             schema=load_schema("search_schema.json"))
    body2 = response.json()
    assert book_title in (body2['payload']['data'][0]['text'])

@allure.title("Поиск книги по неправильному названию")
def test_check_invalid_search():
    wrong_title = 'qwdcvfbetbevsef'
    SEARCH = f'search/suggestions?q={wrong_title}'
    response = get_litress(url=SEARCH, headers={"Content-Type": "application/json"})
    body = response.json()
    validate(body,
             schema=load_schema("search_schema.json"))
    assert wrong_title not in (body['payload']['data'])
