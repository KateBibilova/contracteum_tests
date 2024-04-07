from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url += "/authorization/login"

    def log_in(self):
        print("\nLog in\n")
        self.page.evaluate("localStorage.setItem('mock-client', 'true')")
        self.page.evaluate("localStorage.setItem('i18nextLng', 'ru')")

        self.page.reload()

        self.cert_select_dropdown.click()
        self.venera_cert_option.click()
        self.login_btn.click()
