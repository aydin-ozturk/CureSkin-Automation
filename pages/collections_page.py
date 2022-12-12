from selenium.webdriver.common.by import By
from pages.base_page import Page


class CollectionsPage(Page):
    HEADER = (By.XPATH, "//h1[@class='collection-hero__title']")
    FIRST_PROD_NAME = (By.XPATH, "//main[@id='MainContent']//li[1]//h3[@class='card-information__text h5']")

    def verify_header_is_category_name(self, product_name):
        self.verify_partial_text(product_name, *self.HEADER)

    def verify_first_prod_name_includes_category_name(self, product_name):
        self.verify_partial_text(product_name, *self.FIRST_PROD_NAME)
