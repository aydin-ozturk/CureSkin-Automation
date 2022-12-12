from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    NO_RESULT_MSG = (By.XPATH, "//p[@role='status']")

    def verify_no_result_msg_shown(self, product):
        self.verify_partial_text(f"No results found for “{product}”",*self.NO_RESULT_MSG)