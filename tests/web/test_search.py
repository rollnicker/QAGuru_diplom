from allure_commons._allure import step

from QAGuru_litres.web.application import app


def test_search_book(setup_browser):
    with step('Ввести название в окно поиска'):
        app.header_panel.search_book('Мастер и маргарита')

    with step("открыть книгу в результатах поиска"):
        app.search_page.open_searched_item('Мастер и Маргарита')

    with step("проверить что название книги соответствует поиску"):
        app.item_page.check_book_title('Мастер и Маргарита')


def test_wrong_search(setup_browser):
    with step("Открыть форму логина"):
        app.header_panel.search_book('dgfsergsvers')

    with step("найти книгу в каталоге"):
        app.search_page.check_empty_search_message('ничего не найдено')
