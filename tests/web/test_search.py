import allure

from litres_project.web.application import app


class TestSearch:
    @allure.epic('Search')
    @allure.tag('web', 'positive')
    @allure.title('Поиск книги')
    def test_search_book(self):
        app.open_page()

        app.header_panel.search_book('Мастер и маргарита')
        app.search_page.open_searched_item('Мастер и Маргарита')

        app.item_page.check_book_title('Мастер и Маргарита')

    @allure.epic('Search')
    @allure.tag('web', 'negative')
    @allure.title('Поиск книги с неправильным названием')
    def test_wrong_search(self):
        app.open_page()

        app.header_panel.search_book('dgfsergsvers')

        app.search_page.check_empty_search_message('ничего не найдено')
