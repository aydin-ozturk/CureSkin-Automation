from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage(Page):
    total_price = 0
    product_names = []
    PROD_IMG = (By.XPATH, "//li[1]//modal-opener[1]//div[1]//img[1]")
    PRICE = (By.XPATH, "//*[contains(@id,'price')]//*[@class='price-item price-item--sale price-item--last']")
    REVIEWS = (By.XPATH, "//div[@id='judgeme_product_reviews']//h2[@class='jdgm-rev-widg__title']")
    QUANTITY = (By.XPATH, "//div[@class='product-form__input product-form__quantity']/label")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@name='add']")
    BUY_IT_NOW_BTN = (By.XPATH, "//button[contains(text(),'Buy it now')]")
    CART = (By.ID, "cart-icon-bubble")
    CART_POP_UP_IMG = (By.XPATH, "//img[@class='cart-notification-product__image']")
    PROD_NAME = (By.XPATH, "//h1[@class='product__title']")

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
        self.find_element(*self.ADD_TO_CART_BTN)

        # Verifying buy it now button presence
        self.find_element(*self.BUY_IT_NOW_BTN)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait.until(EC.presence_of_element_located(self.CART_POP_UP_IMG))

    def click_on_cart(self):
        self.click(*self.CART)

    def sum_and_store_product_prices(self):
        self.total_price += float(self.find_element(*self.PRICE).text[4:])
        self.driver.total_price = self.total_price

    def store_product_names(self):
        self.product_names.append(self.find_element(*self.PROD_NAME).text)
        self.driver.product_names = self.product_names
