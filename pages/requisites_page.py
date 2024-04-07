from playwright.sync_api import Page, expect

from data.test_data import *
from .base_page import BasePage


class RequisitesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url += "/organization/requisites"
        self.title = self.page.locator(".Organization_title__i3Oia")

        self.org_id = self.page.locator(".Organization_wrapper-attr__oYqit")
        self.edit_btn = self.page.locator("button[class*='Organization_button']")

        # REQUISITES
        self.ogrn = self.page.locator("xpath=(//*[@class='organization-attributes_value__sTPyY'])[1]")
        self.inn = self.page.locator("xpath=(//*[@class='organization-attributes_value__sTPyY'])[2]")
        self.kpp = self.page.locator("xpath=(//*[@class='organization-attributes_value__sTPyY'])[3]")
        self.address = self.page.locator("xpath=//*[text()='Юридический Адрес']/following-sibling::*")
        self.postal_address = self.page.locator("xpath=(//*[text()='Почтовый адрес']/following-sibling::*)[1]")
        self.email = self.page.locator("xpath=(//*[text()='E-mail']/following-sibling::*)[1]")
        self.phone = self.page.locator("xpath=(//*[text()='Телефон']/following-sibling::*)[1]")
        self.bank_name = self.page.locator("xpath=//*[text()='Наименование банка']/following-sibling::*")
        self.bank_dept_name = self.page.locator(
            "xpath=(//*[text()='Наименование отделения банка']/following-sibling::*)[1]")
        self.payment_account = self.page.locator("xpath=(//*[text()='Расчётный счёт']/following-sibling::*)[1]")
        self.corr_account = self.page.locator("xpath=//*[text()='Корреспондентский счет']/following-sibling::*")
        self.bic = self.page.locator("xpath=(//*[text()='БИК']/following-sibling::*)[1]")

        # SUCCESS POPUP
        self.save_success_popup = self.page.locator("xpath=//*[text()='Банковские реквизиты успешно обновлены']")
        self.close_popup_btn = self.page.locator("xpath=//*[@id='__react-alert__']//*[@role='button']")

    def open(self):
        print("\nOpen requisites page\n")
        self.page.goto(self.url)
        expect(self.title).to_be_visible()
        expect(self.org_id).to_be_visible()

    def open_edit_sidebar(self):
        print("\nOpen edit sidebar\n")
        self.edit_btn.click()
        expect(
            self.page.locator("[class*='aside-organization_wrapper']")
            .filter(has_text="Редактирование"),
            message="Edit sidebar should be visible"
        ).to_be_visible()

    def verify_saved_info(self):
        print("\nVerify saved info\n")
        expect(self.ogrn).to_have_text(OGRN)
        expect(self.inn).to_have_text(INN)
        expect(self.kpp).to_have_text(KPP)
        expect(self.address).to_have_text(f"{RUSSIA_CODE}, {ADDRESS}")
        expect(self.postal_address).to_have_text(f"{RUSSIA_CODE}, {POSTAL_ADDRESS}")
        expect(self.email).to_have_text(EMAIL)
        expect(self.phone).to_have_text(f"+7 ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:]}")
        expect(self.bank_name).to_have_text(BANK_NAME)
        expect(self.bank_dept_name).to_have_text(BANK_DEPT)
        expect(self.payment_account).to_have_text(PAYMENT_ACCOUNT)
        expect(self.corr_account).to_have_text(CORR_ACCOUNT)
        expect(self.bic).to_have_text(BIC)

    def verify_success_popup(self):
        print("\nVerify success popup\n")
        expect(self.save_success_popup).to_be_visible()
        self.close_popup_btn.click()
        expect(self.save_success_popup).not_to_be_visible()

    def get_requisites(self) -> dict:
        print("\nGet requisites\n")
        requisites = {
            "OGRN": OGRN,
            "INN": INN,
            "KPP": self.kpp.text_content(),
            "PHONE": self.phone.text_content(),
            "EMAIL": self.email.text_content(),
            "ADDRESS": self.address.text_content(),
            "POSTAL_ADDRESS": self.postal_address.text_content(),
            "BANK_DEPT": self.bank_dept_name.text_content(),
            "BANK_NAME": self.bank_name.text_content(),
            "PAYMENT_ACCOUNT": self.payment_account.text_content(),
            "CORR_ACCOUNT": self.corr_account.text_content(),
            "BIC": self.bic.text_content()
        }

        return requisites

    def compare_actual_and_initial_requisites(self, initial_requisites):
        print("\nCompare actual and initial requisites\n")
        expect(self.ogrn).to_have_text(initial_requisites["OGRN"])
        expect(self.inn).to_have_text(initial_requisites["INN"])
        expect(self.kpp).to_have_text(initial_requisites["KPP"])
        expect(self.address).to_have_text(initial_requisites['ADDRESS'])
        expect(self.postal_address).to_have_text(initial_requisites["POSTAL_ADDRESS"])
        expect(self.email).to_have_text(initial_requisites["EMAIL"])
        expect(self.phone).to_have_text(initial_requisites["PHONE"])
        expect(self.bank_name).to_have_text(initial_requisites["BANK_NAME"])
        expect(self.bank_dept_name).to_have_text(initial_requisites["BANK_DEPT"])
        expect(self.payment_account).to_have_text(initial_requisites["PAYMENT_ACCOUNT"])
        expect(self.corr_account).to_have_text(initial_requisites["CORR_ACCOUNT"])
        expect(self.bic).to_have_text(initial_requisites["BIC"])
