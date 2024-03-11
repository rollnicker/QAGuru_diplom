import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ProfilePage:
    def __init__(self):
        self.login_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button'))
        self.login_edit = browser.element((AppiumBy.ID, 'ru.litres.android:id/loginEditText'))
        self.login_continue_button = browser.element((AppiumBy.ID, 'ru.litres.android:id/continueButton'))
        self.password_edit = browser.element((AppiumBy.ID, 'ru.litres.android:id/passwordEditText'))
        self.profile_name = browser.element((AppiumBy.ID, 'ru.litres.android:id/user_login'))

    @allure.step('Нажать кнопку "login"')
    def open_login(self):
        self.login_button.click()

    def enter_email(self, email):
        with allure.step(f'Ввести email: {email}'):
            self.login_edit.type(email)
            self.login_continue_button.click()

    def enter_password(self, password):
        with allure.step(f'Ввести email: {password}'):
            self.password_edit.type(password)
            self.login_continue_button.click()

    def check_profile_name(self, name):
        with allure.step(f'Проверить что логин {name} совпадает с введенным'):
            self.profile_name.should(have.text(name))
