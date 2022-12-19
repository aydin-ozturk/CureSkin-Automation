from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    stored_total_product_price = None
    PLUS_ICON = (By.NAME, "plus")
    PRODUCT_QTY_1 = (By.ID, "Quantity-1")
    PRODUCT_TOTAL = (By.XPATH, "//table[@class='cart-items']/tbody//tr[1]//*[@class='cart-item__totals right small-hide']")
    NEW_SUBTOTAL_HIDDEN = (By.XPATH, "//p[contains(text(),'New subtotal')]")
    SUBTOTAL = (By.XPATH, "//p[@class='totals__subtotal-value']")
    CART_COUNT = (By.XPATH, "//span[normalize-space()='2']")
    FIRST_PROD_NAME = (By.XPATH, "//tr[@id='CartItem-2']/td[2]/a")
    SECOND_PROD_NAME = (By.XPATH, "//tr[@id='CartItem-1']/td[2]/a")
    ALL_PRODUCTS = (By.XPATH, "//tr[@class='cart-item']//td[@class='cart-item__details']/a")
    VIEW_ALL_BTN = (By.XPATH, "//a[@aria-label='View all products in the Products collection']")

    def store_cart_total(self):
        self.stored_total_product_price = float(self.find_element(*self.PRODUCT_TOTAL).text[4:])

    def click_on_plus_icon(self):
        self.click(*self.PLUS_ICON)

    def verify_cart_total_doubled(self):
        # Wait for cart to be updated
        self.find_element(*self.NEW_SUBTOTAL_HIDDEN)

        current_total_product_price = float(self.find_element(*self.PRODUCT_TOTAL).text[4:])
        assert self.stored_total_product_price * 2 == current_total_product_price, \
            f"Expected {self.stored_total_product_price * 2} but got {current_total_product_price}"

    def verify_product_quantity(self):
        quantity = 2
        updated_quantity = int(self.driver.find_element(*self.PRODUCT_QTY_1).get_attribute("value"))
        assert updated_quantity == quantity, f"Expected, {quantity} but got {updated_quantity}"

    def verify_all_products_in_cart(self):
        all_products = self.find_elements(*self.ALL_PRODUCTS)
        product_names = []
        for product in all_products:
            product_names.insert(0, product.text)
        assert product_names == self.driver.product_names, f"Product names do not match \
        \nExpected {self.driver.product_names} but got {product_names}"

    def verify_total_cart_price(self):
        cart_subtotal = float(self.find_element(*self.SUBTOTAL).text[4:])
        assert cart_subtotal == self.driver.total_price, \
            f"Incorrect cart total \
            \nExpected {self.driver.total_price} but got {cart_subtotal}"

    def open_cart_page(self):
        self.open_url("cart")

    def click_on_view_all_btn(self):
        self.click(*self.VIEW_ALL_BTN)
