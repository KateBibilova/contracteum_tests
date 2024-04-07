from playwright.sync_api import Page, expect

from .base_page import BasePage


class ContractsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url += "/contracts"
        self.contracts_title = self.page.get_by_text("Договоры").nth(1)

    def assert_open(self):
        print("\nAssert contracts page is open\n")
        expect(self.contracts_title).to_be_visible()
