import allure
from allure_commons._allure import step

from QAGuru_litres.web.application import app


@allure.epic('Favourites')
@allure.tag('web', 'positive')
@allure.title('Добавление книги в избранное')
def test_add_to_favourites(setup_browser):
    with step('Открыть категорию каталога'):
        app.header_panel.open_catalog_category("Легкое чтение")

    with step("выбрать книгу из каталога"):
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')

    with step('Нажать кнопку отложить'):
        app.item_page.add_book_for_later()

    with step('проверить что счетчик "отложенные" отображает количество книг'):
        app.header_panel.check_items_count("1")

    with step('Открыть страницу "отложенные'):
        app.header_panel.open_liked_books()

    with step('Проверить что отложенная книга отображается в списке'):
        app.favourite_page.check_first_liked_book_title('Туман. Полное издание')


@allure.epic('Favourites')
@allure.tag('web', 'positive')
@allure.title('Удалить книгу из избранного')
def test_delete_from_favourites(setup_browser):
    with step('Открыть категорию каталога'):
        app.header_panel.open_catalog_category("Легкое чтение")

    with step("выбрать книгу из каталога"):
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')

    with step('Нажать кнопку отложить'):
        app.item_page.add_book_for_later()

    with step('проверить что счетчик "отложенные" отображает количество книг'):
        app.header_panel.check_items_count("1")

    with step('Нажать кнопку отложить'):
        app.item_page.add_book_for_later()

    with step('проверить что счетчик "отложенные" исчез'):
        app.header_panel.check_count_is_empty()

    with step('Открыть страницу "отложенные'):
        app.header_panel.open_liked_books()

    with step('проверить что книга больше не в избранном'):
        app.favourite_page.check_no_favourite_books_message('Здесь будет все, что вы отложите на потом')
