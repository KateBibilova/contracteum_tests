from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://demo.contracteum.com"

    def __init__(self, page: Page):
        self.url = self.BASE_URL
        self.page = page

        self.cert_select_dropdown = self.page.locator(".css-hlgwow")
        self.venera_cert_option = self.page.locator("#react-select-2-option-0")
        self.login_btn = self.page.locator("button[class*=LoginPage_button]")
        self.org_dropdown = self.page.locator("xpath=//*[text()='Организация']")
        self.org_profile_link = self.page.locator("[href='/organization/requisites']")

    def open(self):
        print("\n\nOpen page\n")
        self.page.goto(self.url)
