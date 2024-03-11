import allure
from selene import browser

from litres_project.web.components.header_panel import HeaderPanel
from litres_project.web.components.login import LoginWindow
from litres_project.web.pages.cart_page import CartPage
from litres_project.web.pages.catalog_page import CatalogPage
from litres_project.web.pages.favourite_page import FavouritePage
from litres_project.web.pages.item_page import ItemPage
from litres_project.web.pages.profile_page import ProfilePage
from litres_project.web.pages.search_page import SearchPage


class Application:

    def __init__(self):
        self.header_panel = HeaderPanel()
        self.login_window = LoginWindow()
        self.profile_page = ProfilePage()
        self.search_page = SearchPage()
        self.item_page = ItemPage()
        self.catalog_page = CatalogPage()
        self.favourite_page = FavouritePage()
        self.cart_page = CartPage()

    @allure.step('Открыть сайт litres')
    def open_page(self):
        browser.open('')
        return self


app = Application()
