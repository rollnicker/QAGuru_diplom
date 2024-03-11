from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class FavouritesPage:
    def __init__(self):
        self.close_banner_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/btnMyBooksOnboardingClose'))
        self.favorites_section_button = browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookSectionTitle'))[0]
        self.favorites_books_list = browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookName'))

    def close_banner(self):
        self.close_banner_button.click()

    def open_favorites_books(self):
        self.favorites_section_button.click()

    def check_favorite_book_title(self, title):
        self.favorites_books_list[0].should(have.text(title))
