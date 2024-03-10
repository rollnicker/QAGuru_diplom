from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class MainPage:
    def __init__(self):
        self.language_choice_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton'))
        self.erotic_banner_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent'))
        self.profile_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item'))
        self.search_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/search'))
        self.favourites_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/nav_my_audiobooks'))

    def choose_language(self):
        if self.language_choice_button.should(be.existing):
            self.language_choice_button.click()
        else:
            pass

    def close_erotic_banner(self):
        if self.erotic_banner_button.should(be.existing):
            self.erotic_banner_button.click()
        else:
            pass

    def open_profile_page(self):
        self.profile_button.click()

    def open_search_page(self):
        self.search_button.click()

    def open_favourites(self):
        self.favourites_button.click()
