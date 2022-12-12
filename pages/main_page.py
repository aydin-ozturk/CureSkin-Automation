from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
    SEARCH_INPUT = (By.ID, "Search-In-Modal")
    BY_CATEGORY = (By.XPATH, "//details[@id='Details-HeaderMenu-3']")
    ALL_CATEGORIES = (By.XPATH, "//ul[@id='HeaderMenu-MenuList-3']//li")
    PROFILE_ICON = (By.XPATH, "//a[@class='header__icon header__icon--account link focus-inset small-hide']")

    def open_main_page(self):
        self.open_url()

    def search(self, product):
        self.click(*self.SEARCH_ICON)
        self.input_text(product, *self.SEARCH_INPUT)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def click_on_shop_by_category(self):
        self.click(*self.BY_CATEGORY)

    def click_on_category_name(self, category_name):
        all_categories = self.find_elements(*self.ALL_CATEGORIES)
        locator_index = None
        for n in range(len(all_categories)):
            if all_categories[n].text == category_name:
                locator_index = n
        self.find_elements(*self.ALL_CATEGORIES)[locator_index].click()

    def click_on_profile_icon(self):
        self.click(*self.PROFILE_ICON)


