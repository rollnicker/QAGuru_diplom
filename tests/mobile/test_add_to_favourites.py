import allure
from allure_commons._allure import step

from litres_project.mobile.application import mob_app


@allure.epic('Favourites')
@allure.tag('mobile', 'positive')
@allure.title('Добавление книги в избранное')
def test_add_book_to_favourites(android_mobile_management):
    with step('Закрыть выбор языка'):
        mob_app.main_page.choose_language()
    with step('Закрыть всплывающее окно выбора эротики'):
        mob_app.main_page.close_erotic_banner()

    with step('Открыть страницу поиска'):
        mob_app.main_page.open_search_page()
    with step('Ввести название книги в поисковую строку'):
        mob_app.search_page.search_book(name='Мастер и маргарита')
    with step('Добавить первую книгу в избранное'):
        mob_app.search_page.add_searched_book_to_favourites()
    with step('Открыть первую книгу'):
        mob_app.search_page.open_searched_book()
    with step('Открыть вкладку избранное'):
        mob_app.main_page.open_favourites()
    with step('Закрыть всплывающее окно'):
        mob_app.favourites_page.close_banner()
    with step('Выбрать раздел избранное'):
        mob_app.favourites_page.open_favorites_books()

    with step('Проверить название выбранной книги присутствует в избранном поиску'):
        mob_app.favourites_page.check_favorite_book_title(title="Мастер и Маргарита")
