from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    EMAIL_INPUT = (By.ID, "CustomerEmail")
    PASSWORD_INPUT = (By.ID, "CustomerPassword")
    SIGN_IN = (By.XPATH, "//button[contains(text(), 'Sign in')]")
    CREATE_ACCOUNT = (By.XPATH, "//a[@href='/account/register']")
    LOGIN_TXT = (By.XPATH, "//h1[@id='login']")

    def verify_login_page_opened(self):
        self.verify_partial_text("Login", *self.LOGIN_TXT)
        self.verify_url_contains_query("account/login")