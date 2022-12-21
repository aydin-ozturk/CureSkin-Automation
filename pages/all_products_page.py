from selenium.webdriver.common.by import By
from pages.base_page import Page


class AllProductsPage(Page):
    PRODUCTS_HEADER = (By.XPATH, "//h1[@class='collection-hero__title']")
    FIRST_PRODUCT = (By.XPATH, "//*[@id='product-grid']//li[1]//h3/a")
    CHAT_FRAME = (By.XPATH, "//iframe[@id='dummy-chat-button-iframe']")
    CHAT_MSG_COUNT = (By.XPATH, "//span[@id='notification-badge' and @style='visibility: visible;']")

    def wait_for_chat_popup(self):
        chat_frame = self.find_element(*self.CHAT_FRAME)
        self.driver.switch_to.frame(chat_frame)
        self.wait_for_element_appear(*self.CHAT_MSG_COUNT)
        self.driver.switch_to.default_content()

    def verify_all_products_page_opened(self):
        self.verify_url_contains_query("collections/all")
        self.verify_partial_text("Products", *self.PRODUCTS_HEADER)

    def click_first_product(self):
        self.wait_for_chat_popup()
        self.click(*self.FIRST_PRODUCT)
