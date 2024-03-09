from allure_commons._allure import step

from QAGuru_litres.web.application import app


def test_add_to_favourite_from_delete_window(setup_browser):
    with step('Открыть категорию каталога'):
        app.header_panel.open_catalog_category("Легкое чтение")

    with step("выбрать книгу из каталога"):
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')

    with step('Нажать кнопку "добавить в корзину"'):
        app.item_page.add_book_to_cart()

    with step("открыть коризну"):
        app.item_page.open_cart()

    with step('Проверить наличие книги в корзине'):
        app.cart_page.check_title('Туман. Полное издание')

    with step('Удалить из корзины'):
        app.cart_page.click_delete_button()

    with step('Добавить в отложенные'):
        app.cart_page.add_to_later_list()

    with step('Открыть отложенные'):
        app.header_panel.open_liked_books()

    with step('Проверить что книга отображается в отложенных'):
        app.favourite_page.check_first_liked_book_title('Туман. Полное издание')
