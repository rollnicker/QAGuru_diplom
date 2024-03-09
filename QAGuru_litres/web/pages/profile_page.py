from selene import browser, have


class ProfilePage:
    def __init__(self):
        self.avatar_name = browser.element('.Avatar-module__topContent_vxotx')

    def avatar_should_have_name(self, name):
        self.avatar_name.should(have.text(name))
