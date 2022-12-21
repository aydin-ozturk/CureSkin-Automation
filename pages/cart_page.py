from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    stored_total_product_price = None
    PLUS_ICON = (By.NAME, "plus")
    PRODUCT_QTY = (By.ID, "Quantity-1")
    PRODUCT_TOTAL = (By.XPATH, "//table[@class='cart-items']/tbody//tr[1]//*[@class='cart-item__totals right small-hide']")
    UPDATED_SUBTOTAL_HIDDEN = (By.XPATH, "//p[@id='cart-live-region-text' and @aria-hidden='true']")
    SUBTOTAL = (By.XPATH, "//p[@class='totals__subtotal-value']")
    ALL_PRODUCTS = (By.XPATH, "//tr[@class='cart-item']//td[@class='cart-item__details']/a")
    VIEW_ALL_BTN = (By.XPATH, "//a[@aria-label='View all products in the Products collection']")
    CHAT_BTN = (By.ID, "dummy-chat-button-iframe")
    CHAT_FRAME = (By.XPATH, "//iframe[@id='dummy-chat-button-iframe']")
    CHAT_MSG_COUNT = (By.XPATH, "//span[@id='notification-badge' and @style='visibility: visible;']")

    def wait_for_chat_popup(self):
        chat_frame = self.find_element(*self.CHAT_FRAME)
        self.driver.switch_to.frame(chat_frame)
        self.wait_for_element_appear(*self.CHAT_MSG_COUNT)
        self.driver.switch_to.default_content()

    def store_cart_total(self):
        self.stored_total_product_price = float(self.find_element(*self.PRODUCT_TOTAL).text[4:])

    def click_on_plus_icon(self):
        self.wait_for_chat_popup()
        self.click(*self.PLUS_ICON)

    def verify_cart_total_doubled(self):
        # Wait for cart to be updated
        self.find_element(*self.UPDATED_SUBTOTAL_HIDDEN)

        current_total_product_price = float(self.find_element(*self.PRODUCT_TOTAL).text[4:])
        assert self.stored_total_product_price * 2 == current_total_product_price, \
            f"Expected {self.stored_total_product_price * 2} but got {current_total_product_price}"

    def verify_product_quantity(self):
        quantity = 2
        updated_quantity = int(self.driver.find_element(*self.PRODUCT_QTY).get_attribute("value"))
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
