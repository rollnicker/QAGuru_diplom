from selene import browser, have


class CartPage:
    def __init__(self):
        self.book_title = browser.all('[data-testid="cart__bookCardTitle--wrapper"]')[0]
        self.delete_button = browser.element('[data-testid="cart__listDeleteButton--desktop"]')
        self.confirm_delete_button = browser.all('.Modal-module__controls_1qN-h button')[0]
        self.add_to_later_from_delete_button = browser.all('.Modal-module__controls_1qN-h button')[1]
        self.empty_cart_module = browser.element('.EmptyState-module__empty__title_22qdT')

    def check_title(self, name):
        self.book_title.should(have.text(name))

    def click_delete_button(self):
        self.delete_button.click()

    def confirm_delete_item(self):
        self.confirm_delete_button.click()

    def add_to_later_list(self):
        self.add_to_later_from_delete_button.click()

    def check_empty_cart_message(self, text):
        self.empty_cart_module.should(have.text(text))


