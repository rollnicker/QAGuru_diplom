from selene import browser, have


class CatalogPage:
    def __init__(self):
        self.catalog_category_books = browser.all('[data-testid="art__wrapper"]')

    def open_book_from_catalog(self, name):
        self.catalog_category_books.element_by(have.text(name)).click()
