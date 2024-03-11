import allure
from selene import browser, have


class CartPage:
    def __init__(self):
        self.book_title = browser.all('[data-testid="cart__bookCardTitle--wrapper"]')[0]
        self.delete_button = browser.element('[data-testid="cart__listDeleteButton--desktop"]')
        self.confirm_delete_button = browser.all('.Modal-module__controls_1qN-h button')[0]
        self.add_to_later_from_delete_button = browser.all('.Modal-module__controls_1qN-h button')[1]
        self.empty_cart_module = browser.element('.EmptyState-module__empty__title_22qdT')

    def check_title(self, name):
        with allure.step(f'Проверить что название книги "{name}" отображается в корзине'):
            self.book_title.should(have.text(name))

    @allure.step('Нажать кнопку удалить')
    def click_delete_button(self):
        self.delete_button.click()

    @allure.step('Подтвердить удаление')
    def confirm_delete_item(self):
        self.confirm_delete_button.click()

    @allure.step('Нажать кнопку "отложить и удалить"')
    def add_to_later_list(self):
        self.add_to_later_from_delete_button.click()

    def check_empty_cart_message(self, text):
        with allure.step(f'Проверить что появилось сообщение "{text}"'):
            self.empty_cart_module.should(have.text(text))
