import allure
from selene import browser, have, command


class ItemPage:
    def __init__(self):
        self.book_title = browser.element('h1.BookCard-module__book__mainInfo__title_2zz4M')
        self.later_button = browser.all('[type="button"]').element_by(have.text('Отложить'))
        self.add_to_cart_button = browser.element('[data-testid="book__addToCartButton--desktop"]')
        self.modal_close_button = browser.element('[data-testid="modal__close--button"]')
        self.go_to_cart_button = browser.element('[data-testid="book__goToCartButton--desktop"]')

    def check_book_title(self, name):
        with allure.step(f'Проверить что название книги "{name}" соответствует поиску'):
            self.book_title.should(have.text(name))

    @allure.step('Нажать кнопку отложить')
    def add_book_for_later(self):
        self.later_button.click()

    @allure.step('Нажать кнопку "добавить в корзину"')
    def add_book_to_cart(self):
        self.add_to_cart_button.perform(command.js.scroll_into_view).click()
        self.modal_close_button.click()

    @allure.step("открыть корзину")
    def open_cart(self):
        self.go_to_cart_button.should(have.text("В корзине")).click()
