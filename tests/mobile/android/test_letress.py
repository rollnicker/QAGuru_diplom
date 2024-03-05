from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_check_welcome_screens(android_mobile_management):
    with (step('Skip welcome screens')):
        with step('закрыть крестик'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).click()
        with step('открыть поиск'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
        with step('ввести слово в поиск'):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Мастер и маргарита')
        with step('Выбрать книгу'):
            browser.all((AppiumBy.ID, 'ru.litres.android:id/clArtLayout'))[0].click()