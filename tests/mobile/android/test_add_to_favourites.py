from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_add_book_to_favourites(android_mobile_management):
    with step('закрыть выбор языка'):
        if browser.element('ru.litres.android:id/choosebutton').should(be.existing):
            browser.element('ru.litres.android:id/choosebutton').click()
        else:
            pass
    with step('закрыть крестик'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).click()
    with step('открыть поиск'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
    with step('ввести слово в поиск'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Мастер и маргарита')
    with step('Выбрать текстовый элемент из списка'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText'))[0].click()
    with step('Добавить первую книгу в избранное'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/imageViewFavorite'))[0].click()
    with step('Открыть первую книгу'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/clArtLayout'))[0].click()
    with step('Открыть вкладку избранное'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/nav_my_audiobooks')).click()
    with step('Закрыть всплывающее окно'):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnMyBooksOnboardingClose')).click()
    with step('Выбрать раздел избранное'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookSectionTitle'))[0].click()
    with step('Проверить название выбранной книги присутствует в избранном поиску'):
        browser.all((AppiumBy.ID, 'ru.litres.android:id/textViewBookName'))[0].should(have.text("Мастер и Маргарита"))
