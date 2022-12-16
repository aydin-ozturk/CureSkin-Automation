from selenium.webdriver.common.by import By
from pages.base_page import Page


class AllProductsPage(Page):
    PRODUCTS_HEADER = (By.XPATH, "//h1[@class='collection-hero__title']")

    def verify_all_products_page_opened(self):
        self.verify_url_contains_query("collections/all")
        self.verify_partial_text("Products", *self.PRODUCTS_HEADER)