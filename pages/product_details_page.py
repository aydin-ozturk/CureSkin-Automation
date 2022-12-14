from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductDetailsPage(Page):
    PROD_IMG = (By.XPATH, "//li[1]//modal-opener[1]//div[1]//img[1]")
    PRICE = (By.XPATH, "//*[contains(@id,'price')]//*[@class='price-item price-item--sale price-item--last']")
    REVIEWS = (By.XPATH, "//div[@id='judgeme_product_reviews']//h2[@class='jdgm-rev-widg__title']")
    QUANTITY = (By.XPATH, "//div[@class='product-form__input product-form__quantity']/label")
    ADD_TO_CART = (By.XPATH, "//button[@name='add']")
    BUY_IT_NOW = (By.XPATH, "//button[contains(text(),'Buy it now')]")

    def verify_ui_elements_present(self):
        # Verifying product image presence
        self.find_element(*self.PROD_IMG)

        # Verifying product price presence
        self.verify_partial_text("Rs", *self.PRICE)

        # Verifying product reviews presence
        self.verify_element_text("Customer Reviews", *self.REVIEWS)

        # Verifying product quantity presence
        self.verify_element_text("Quantity", *self.QUANTITY)

        # Verifying add to cart button presence
        self.find_element(*self.ADD_TO_CART)

        # Verifying buy it now button presence
        self.find_element(*self.BUY_IT_NOW)


