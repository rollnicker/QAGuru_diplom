import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class FavouritesPage:
    def __init__(self):
        self.close_banner_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/btnMyBooksOnboardingClose'))
        self.favorites_section_button = browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookSectionTitle'))[0]
        self.favorites_books_list = browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookName'))

    @allure.step('Закрыть всплывающее окно')
    def close_banner(self):
        self.close_banner_button.click()

    @allure.step('Выбрать раздел избранное')
    def open_favorites_books(self):
        self.favorites_section_button.click()

    def check_favorite_book_title(self, title):
        with allure.step(f'Проверить название "{title}" выбранной книги присутствует в избранном поиску'):
            self.favorites_books_list[0].should(have.text(title))
