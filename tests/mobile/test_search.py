import allure
from allure_commons._allure import step

from litres_project.mobile.application import mob_app


@allure.epic('Search')
@allure.tag('mobile', 'positive')
@allure.title('Поиск книги по названию')
def test_search_book(android_mobile_management):
    with step('Закрыть выбор языка'):
        mob_app.main_page.choose_language()
    with step('Закрыть всплывающее окно выбора эротики'):
        mob_app.main_page.close_erotic_banner()

    with step('Открыть страницу поиска'):
        mob_app.main_page.open_search_page()
    with step('Ввести название книги в поисковую строку'):
        mob_app.search_page.search_book(name='Мастер и маргарита')
    with step('Выбрать первую книгу из результатов поиска'):
        mob_app.search_page.open_searched_book()

    with step('Проверить, что название выбранной книги соответствует поиску'):
        mob_app.item_page.check_book_title(title='Мастер и Маргарита')
