from allure_commons._allure import step

from QAGuru_litres.web.application import app


def test_add_to_cart(setup_browser):
    with step('Открыть категорию каталога'):
        app.header_panel.open_catalog_category("Легкое чтение")

    with step("выбрать книгу из каталога"):
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')

    with step('Нажать кнопку "добавить в корзину"'):
        app.item_page.add_book_to_cart()

    with step('проверить что счетчик "отложенные" отображает количество книг'):
        app.header_panel.check_items_count("1")

    with step("открыть корзину"):
        app.item_page.open_cart()

    with step('Проверить наличие книги в корзине'):
        app.cart_page.check_title('Туман. Полное издание')


def test_delete_item_from_cart(setup_browser):
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
        app.cart_page.confirm_delete_item()

    with step('Проверить что книга больше не в корзине'):
        app.cart_page.check_empty_cart_message('Корзина пуста')
