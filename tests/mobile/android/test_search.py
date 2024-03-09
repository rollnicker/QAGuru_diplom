import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be

@allure.epic('Search')
@allure.tag('mobile', 'positive')
@allure.title('Поиск книги по названию')
def test_search_book(android_mobile_management):
    with step('закрыть выбор языка'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
    with step('закрыть всплывающее окно выбора эротики'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent')).click()
    # with step('закрыть крестик'):
    #     browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).click()
    with step('открыть поиск'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
    with step('ввести слово в поиск'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Мастер и маргарита')
    with step('Выбрать элемент из списка'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText'))[0].click()
    with step('Выбрать вариант из предложенного списка'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/clArtLayout'))[0].click()
    with step('Проверить название выбранной книги соответствует поиску'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/tvBookTitle')
                        ).should(have.text("Мастер и Маргарита"))
