from selene import browser

from litres_project.mobile.pages.favourites_page import FavouritesPage
from litres_project.mobile.pages.item_page import ItemPage
from litres_project.mobile.pages.main_page import MainPage
from litres_project.mobile.pages.profile_page import ProfilePage
from litres_project.mobile.pages.search_page import SearchPage


class Application:

    def __init__(self):
        self.main_page = MainPage()
        self.profile_page = ProfilePage()
        self.search_page = SearchPage()
        self.item_page = ItemPage()
        self.favourites_page = FavouritesPage()


mob_app = Application()
