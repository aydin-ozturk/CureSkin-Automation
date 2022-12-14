from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.collections_page import CollectionsPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.all_products_page import AllProductsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.collections_page = CollectionsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.all_products_page = AllProductsPage(self.driver)