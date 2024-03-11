from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SearchPage:
    def __init__(self):
        self.search_window = browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
        self.suggest_list = browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText'))
        self.searched_books_list = browser.all((AppiumBy.ID, 'ru.litres.android:id/clArtLayout'))
        self.favourite_buttons_list = browser.all((AppiumBy.ID, 'ru.litres.android:id/imageViewFavorite'))

    def search_book(self, name):
        self.search_window.type(name)
        self.suggest_list[0].click()

    def open_searched_book(self):
        self.searched_books_list[0].click()

    def add_searched_book_to_favourites(self):
        self.favourite_buttons_list[0].click()
