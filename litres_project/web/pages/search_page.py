import allure
from selene import browser, have


class SearchPage:
    def __init__(self):
        self.search_results = browser.all('.ArtInfo-modules__title_1UysF')
        self.empty_search = browser.element('[data-testid="search-title__wrapper"]')

    def open_searched_item(self, name):
        with allure.step(f'Открыть книгу "{name}" в результатах поиска'):
            self.search_results.element_by(have.text(name)).click()

    def check_empty_search_message(self, text):
        with allure.step(f'Проверить что появилось сообщение "{text}"'):
            self.empty_search.should(have.text(text))
