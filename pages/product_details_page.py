from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage(Page):
    product_price_1 = None
    product_price_2 = None
    product_name_1 = None
    product_name_2 = None
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

    def store_first_product_price(self):
        self.driver.product_price_1 = float(self.find_element(*self.PRICE).text[4:])

    def store_second_product_price(self):
        self.driver.product_price_2 = float(self.find_element(*self.PRICE).text[4:])

    def store_first_product_name(self):
        self.driver.product_name_1 = self.find_element(*self.PROD_NAME).text

    def store_second_product_name(self):
        self.driver.product_name_2 = self.find_element(*self.PROD_NAME).text
