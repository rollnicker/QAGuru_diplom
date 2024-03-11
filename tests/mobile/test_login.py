import os

import allure
from allure_commons._allure import step

from litres_project.mobile.application import mob_app


@allure.epic('Login')
@allure.tag('mobile', 'positive')
@allure.title('Авторизация в приложении')
def test_login(android_mobile_management):
    with step('закрыть выбор языка'):
        mob_app.main_page.choose_language()
    with step('закрыть всплывающее окно выбора эротики'):
        mob_app.main_page.close_erotic_banner()

    with step('Перейти в раздел профиль'):
        mob_app.main_page.open_profile_page()
    with step('Нажать кнопку login'):
        mob_app.profile_page.open_login()
    with step('Ввести email'):
        mob_app.profile_page.enter_email(email=f'{os.getenv("USER_LOGIN")}')
    with step('Ввести пароль'):
        mob_app.profile_page.enter_password(password=f'{os.getenv("USER_PASSWORD")}')

    with step('Проверить успешный логин'):
        mob_app.profile_page.check_profile_name(name=f'{os.getenv("USER_LOGIN")}')
