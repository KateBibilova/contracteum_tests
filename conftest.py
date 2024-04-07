import pytest
from playwright.sync_api import Page

from pages.contracts_page import ContractsPage
from pages.edit_sidebar import EditSidebar
from pages.login_page import LoginPage
from pages.requisites_page import RequisitesPage


@pytest.fixture
def pages(page: Page):
    return ContracteumPages(page)


class ContracteumPages:
    def __init__(self, playwright_page: Page):
        self.login_page = LoginPage(playwright_page)
        self.contracts_page = ContractsPage(playwright_page)
        self.requisites_page = RequisitesPage(playwright_page)
        self.edit_sidebar = EditSidebar(playwright_page)
