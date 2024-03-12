import os

import allure

from litres_project.mobile.application import mob_app


@allure.epic('Login')
@allure.tag('mobile', 'positive')
@allure.title('Авторизация в приложении')
def test_login(android_mobile_management):
    mob_app.main_page.choose_language()
    mob_app.main_page.close_erotic_banner()

    mob_app.main_page.open_profile_page()
    mob_app.profile_page.open_login()
    mob_app.profile_page.enter_email(email=f'{os.getenv("USER_LOGIN")}')
    mob_app.profile_page.enter_password(password=f'{os.getenv("USER_PASSWORD")}')

    mob_app.profile_page.check_profile_name(name=f'{os.getenv("USER_LOGIN")}')
