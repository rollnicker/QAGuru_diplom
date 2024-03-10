from QAGuru_litres.web.components.header_panel import HeaderPanel
from QAGuru_litres.web.components.login import LoginWindow
from QAGuru_litres.web.pages.cart_page import CartPage
from QAGuru_litres.web.pages.catalog_page import CatalogPage
from QAGuru_litres.web.pages.favourite_page import FavouritePage
from QAGuru_litres.web.pages.item_page import ItemPage
from QAGuru_litres.web.pages.profile_page import ProfilePage
from QAGuru_litres.web.pages.search_page import SearchPage


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


app = Application()
