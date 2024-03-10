from QAGuru_litres.mobile.pages.favourites_page import FavouritesPage
from QAGuru_litres.mobile.pages.item_page import ItemPage
from QAGuru_litres.mobile.pages.main_page import MainPage
from QAGuru_litres.mobile.pages.profile_page import ProfilePage
from QAGuru_litres.mobile.pages.search_page import SearchPage


class Application:

    def __init__(self):
        self.main_page = MainPage()
        self.profile_page = ProfilePage()
        self.search_page = SearchPage()
        self.item_page = ItemPage()
        self.favourites_page = FavouritesPage()


mob_app = Application()
