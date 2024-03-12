import allure

from litres_project.mobile.application import mob_app


@allure.epic('Search')
@allure.tag('mobile', 'positive')
@allure.title('Поиск книги по названию')
def test_search_book(android_mobile_management):
    mob_app.main_page.choose_language()
    mob_app.main_page.close_erotic_banner()

    mob_app.main_page.open_search_page()
    mob_app.search_page.search_book(name='Мастер и маргарита')
    mob_app.search_page.open_searched_book()

    mob_app.item_page.check_book_title(title='Мастер и Маргарита')
