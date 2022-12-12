from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
    SEARCH_INPUT = (By.ID, "Search-In-Modal")

    def open_main_page(self):
        self.open_url()

    def search(self, product):
        self.click(*self.SEARCH_ICON)
        self.input_text(product, *self.SEARCH_INPUT)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
