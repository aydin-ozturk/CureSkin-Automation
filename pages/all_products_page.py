from selenium.webdriver.common.by import By
from pages.base_page import Page


class AllProductsPage(Page):
    PRODUCTS_HEADER = (By.XPATH, "//h1[@class='collection-hero__title']")
    FIRST_PRODUCT = (By.XPATH, "//*[@id='product-grid']//li[1]//h3/a")

    def verify_all_products_page_opened(self):
        self.verify_url_contains_query("collections/all")
        self.verify_partial_text("Products", *self.PRODUCTS_HEADER)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT)