from selene import browser, have, be


class HeaderPanel:
    def __init__(self):
        self.login_button = browser.element('[data-testid="tab-login"]')
        self.profile_button = browser.element('.ProfileButton-module__profileButton_2ajQV')
        self.search_window = browser.element('[data-testid="header__search-input--desktop"]')
        self.catalog_button = browser.element('[data-testid="header-catalog-button"]')
        self.catalog_category_list = browser.all('.Column-module__title_1l9dv')
        self.item_count = browser.all('[role="counter"].Counter-modules__counter_1oZcv')
        self.liked_books_button = browser.all('.Tab-modules__tab__title_nqb1J').element_by(have.text("Отложенные"))


    def click_login_button(self):
        self.login_button.click()

    def click_profile_button(self):
        self.profile_button.click()

    def search_book(self, name):
        self.search_window.type(name).submit()

    def open_catalog_category(self, name):
        self.catalog_button.click()
        self.catalog_category_list.element_by(have.text(name)).click()

    def check_items_count(self, count):
        self.item_count[0].should(have.text(count))

    def check_count_is_empty(self):
        self.item_count[0].should(be.absent)

    def open_liked_books(self):
        self.liked_books_button.click()
