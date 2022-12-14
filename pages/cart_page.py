from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC



class CartPage(Page):
    PLUS_ICON = (By.NAME, "plus")
    PRODUCT_QTY_1 = (By.ID, "Quantity-1")
    PRODUCT_TOTAL = (By.XPATH, "//table[@class='cart-items']/tbody//tr[1]//*[@class='cart-item__totals right small-hide']")
    NEW_SUBTOTAL_HIDDEN = (By.XPATH, "//p[contains(text(),'New subtotal')]")
    stored_total_product_price = None

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
