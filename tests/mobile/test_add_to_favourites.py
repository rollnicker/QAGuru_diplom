import allure

from litres_project.mobile.application import mob_app


@allure.epic('Favourites')
@allure.tag('mobile', 'positive')
@allure.title('Добавление книги в избранное')
def test_add_book_to_favourites(android_mobile_management):
    mob_app.main_page.choose_language()
    mob_app.main_page.close_erotic_banner()

    mob_app.main_page.open_search_page()
    mob_app.search_page.search_book(name='Мастер и маргарита')
    mob_app.search_page.add_searched_book_to_favourites()
    mob_app.search_page.open_searched_book()
    mob_app.main_page.open_favourites()
    mob_app.favourites_page.close_banner()
    mob_app.favourites_page.open_favorites_books()

    mob_app.favourites_page.check_favorite_book_title(title="Мастер и Маргарита")
