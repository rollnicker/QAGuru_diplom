from selene import browser, have


class LoginWindow:
    def __init__(self):
        self.email_input = browser.element('[name="email"]')
        self.continue_button = browser.element('.Button-module__button_2hpyT[type="submit"]')
        self.password_input = browser.element('[type="password"]')
        self.wrong_password_warning = browser.element('.ControlInput-module__input__error_2jXOB')
        self.free_email_message = browser.element(
            '.AuthContent-module__emailRegistrationContainer__freeEmailMessage_3np-O')

    def fill_login(self, email):
        self.email_input.type(email)
        self.continue_button.click()

    def fill_login_and_password(self, email, password):
        self.email_input.type(email).submit()
        self.password_input.type(password).submit()

    def check_wrong_password_message(self):
        self.wrong_password_warning.should(have.text('Неверное сочетание логина и пароля'))

    def check_free_email_message(self):
        self.free_email_message.should(have.text('Адрес свободен для регистрации'))

    def check_bad_login_message(self):
        self.wrong_password_warning.should(have.text('Пользователь не найден, чтобы зарегистрироваться укажите почту'))
