from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.collections_page import CollectionsPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.collections_page = CollectionsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)