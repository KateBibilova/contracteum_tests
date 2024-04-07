from playwright.sync_api import Page, expect

from data.test_data import *
from .base_page import BasePage


class EditSidebar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = self.page.locator("[class*='aside-organization_wrapper']").filter(has_text="Редактирование")

        # INPUTS
        self.kpp_input = self.page.locator("input[name='kpp']")
        self.rus_address_dropdown = self.page.locator("xpath=(//*[contains(@class, 'singleValue')])[1]")
        self.address_input = self.page.locator("input[name='address']")
        self.rus_postal_address_dropdown = self.page.locator("xpath=(//*[contains(@class, 'singleValue')])[2]")
        self.postal_address_input = self.page.locator("input[name='postalAddress']")
        self.phone_input = self.page.locator("input[name='phone']")
        self.email_input = self.page.locator("input[name='email']")
        self.bank_name_dropdown = self.page.locator("xpath=(//*[contains(@class, 'singleValue')])[3]")
        self.bank_name_value = self.page.locator("#react-select-2-option-1")
        self.bank_dept_input = self.page.locator("input[name='bankDepartment']")
        self.payment_account_input = self.page.locator("input[name='paymentAccount']")
        self.corr_account_input = self.page.locator("input[name='correspondentAccount']")
        self.bic_input = self.page.locator("input[name='bic']")
        self.save_btn = self.page.locator("[class*='aside-organization_wrapper'] button:nth-child(2)")
        self.cancel_btn = self.page.locator("[class*='aside-organization_wrapper'] button:nth-child(1)")

        # ERRORS
        self.kpp_error = self.page.locator("[name=kpp] + [class*=error-label]")
        self.address_error = self.page.locator("[name=address] + [class*=error-label]")
        self.postal_address_error = self.page.locator("[name=postalAddress] + [class*=error-label]")
        self.phone_error = self.page.locator("[name=phone] + [class*=error-label]")
        self.email_error = self.page.locator("[name=email] + [class*=error-label]")
        self.bank_dept_error = self.page.locator("[name=bankDepartment] + [class*=error-label]")
        self.payment_account_error = self.page.locator("[name=paymentAccount] + [class*=error-label]")
        self.corr_account_error = self.page.locator("[name=correspondentAccount] + [class*=error-label]")
        self.bic_error = self.page.locator("[name=bic] + [class*=error-label]")

    def fill_kpp(self):
        print("\nFill KPP\n")
        self.kpp_input.clear()
        self.kpp_input.fill(KPP)

    def fill_address(self):
        print("\nFill address\n")
        self.address_input.clear()
        self.address_input.fill(ADDRESS)

        expect(
            self.rus_address_dropdown,
            message="Country should be `RUS`"
        ).to_have_text(RUSSIA_CODE)

    def fill_postal_address(self):
        print("\nFill postal address\n")
        self.postal_address_input.clear()
        self.postal_address_input.fill(POSTAL_ADDRESS)

        expect(
            self.rus_postal_address_dropdown,
            message="Country should be `RUS`"
        ).to_have_text(RUSSIA_CODE)

    def fill_contact_info(self):
        print("\nFill contact info\n")
        self.phone_input.clear()
        self.phone_input.fill(PHONE)

        self.email_input.clear()
        self.email_input.fill(EMAIL)

    def fill_bank_info(self):
        print("\nFill bank info\n")
        self.bank_name_dropdown.click()
        self.bank_name_value.click()

        self.bank_dept_input.clear()
        self.bank_dept_input.fill(BANK_DEPT)

        self.payment_account_input.clear()
        self.payment_account_input.fill(PAYMENT_ACCOUNT)

        self.corr_account_input.clear()
        self.corr_account_input.fill(CORR_ACCOUNT)

        self.bic_input.clear()
        self.bic_input.fill(BIC)

    def fill_form(self):
        print("\n<<< FILL FORM >>>\n")
        self.fill_kpp()
        self.fill_address()
        self.fill_postal_address()
        self.fill_contact_info()
        self.fill_bank_info()

    def clear_all_fields(self):
        print("\n<<< CLEAR ALL FIELDS >>>\n")
        self.kpp_input.clear()
        self.address_input.clear()
        self.postal_address_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.bank_dept_input.clear()
        self.payment_account_input.clear()
        self.corr_account_input.clear()
        self.bic_input.clear()

    def save_form(self):
        print("\n<<< SAVE FORM >>>\n")
        self.click_save()

        self.expect_invisible()

    def click_save(self):
        print("\nClick save button\n")
        self.save_btn.click()

    def click_cancel(self):
        print("\nClick cancel button\n")
        self.cancel_btn.click()

    def verify_field_errors(self):
        print("\nVerify field errors\n")
        expect(self.kpp_error).to_have_text(KPP_ERROR)
        expect(self.address_error).to_have_text(ADDRESS_ERROR)
        expect(self.phone_error).to_have_text(PHONE_ERROR)
        expect(self.email_error).to_have_text(EMAIL_ERROR)
        expect(self.bank_dept_error).to_have_text(BANK_DEPT_ERROR)
        expect(self.payment_account_error).to_have_text(PAYMENT_ACCOUNT_ERROR)
        expect(self.corr_account_error).to_have_text(CORR_ACCOUNT_ERROR)
        expect(self.bic_error).to_have_text(BIC_ERROR)

    def expect_invisible(self):
        expect(
            self.page.locator("[class*='aside-organization_wrapper']")
            .filter(has_text="Редактирование"),
            message="Edit sidebar should be invisible"
        ).not_to_be_visible()

    def expect_visible(self):
        expect(
            self.container,
            message="Edit sidebar should be visible"
        ).to_be_visible()
