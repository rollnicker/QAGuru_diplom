from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ItemPage:
    def __init__(self):
        self.book_title = browser.element((AppiumBy.ID, 'ru.litres.android:id/tvBookTitle'))

    def check_book_title(self, title):
        self.book_title.should(have.text(title))
