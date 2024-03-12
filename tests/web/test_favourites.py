import allure

from litres_project.web.application import app


class TestFavourites:
    @allure.epic('Favourites')
    @allure.tag('web', 'positive')
    @allure.title('Добавление книги в избранное')
    def test_add_to_favourites(self):
        app.open_page()

        app.header_panel.open_catalog_category('Легкое чтение')
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')
        app.item_page.add_book_for_later()
        app.header_panel.check_items_count('1')
        app.header_panel.open_liked_books()

        app.favourite_page.check_first_liked_book_title('Туман. Полное издание')

    @allure.epic('Favourites')
    @allure.tag('web', 'positive')
    @allure.title('Удаление книги из избранного')
    def test_delete_from_favourites(self):
        app.open_page()

        app.header_panel.open_catalog_category('Легкое чтение')
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')
        app.item_page.add_book_for_later()
        app.header_panel.check_items_count('1')
        app.item_page.add_book_for_later()
        app.header_panel.check_count_is_empty()
        app.header_panel.open_liked_books()

        app.favourite_page.check_no_favourite_books_message('Здесь будет все, что вы отложите на потом')
