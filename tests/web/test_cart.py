import allure

from litres_project.web.application import app


class TestCart:
    @allure.epic('Cart')
    @allure.tag('web', 'positive')
    @allure.title('Добавление в корзину')
    def test_add_to_cart(self):
        app.open_page()

        app.header_panel.open_catalog_category('Легкое чтение')
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')
        app.item_page.add_book_to_cart()
        app.header_panel.check_items_count('1')
        app.item_page.open_cart()

        app.cart_page.check_title('Туман. Полное издание')

    @allure.epic('Cart')
    @allure.tag('web', 'positive')
    @allure.title('Удаление из корзины')
    def test_delete_item_from_cart(self):
        app.open_page()

        app.header_panel.open_catalog_category("Легкое чтение")
        app.catalog_page.open_book_from_catalog('Туман. Полное издание')
        app.item_page.add_book_to_cart()
        app.item_page.open_cart()
        app.cart_page.check_title('Туман. Полное издание')
        app.cart_page.click_delete_button()
        app.cart_page.confirm_delete_item()

        app.cart_page.check_empty_cart_message('Корзина пуста')
