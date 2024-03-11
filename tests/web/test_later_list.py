import allure

from litres_project.web.application import app


@allure.epic('Favourites')
@allure.tag('web', 'positive')
@allure.title('Добавление книги в отложенные, после удаления из корзины')
def test_add_to_favourite_from_delete_window():
    app.open_page()

    app.header_panel.open_catalog_category("Легкое чтение")

    app.catalog_page.open_book_from_catalog('Туман. Полное издание')

    app.item_page.add_book_to_cart()

    app.item_page.open_cart()

    app.cart_page.check_title('Туман. Полное издание')

    app.cart_page.click_delete_button()

    app.cart_page.add_to_later_list()

    app.header_panel.open_liked_books()

    app.favourite_page.check_first_liked_book_title('Туман. Полное издание')
