import pytest

class TestEditForm:
    def setup(self, pages):
        pages.login_page.open()
        pages.login_page.log_in()

        pages.contracts_page.assert_open()

        pages.requisites_page.open()
        pages.requisites_page.open_edit_sidebar()

    def setup_initial_requisites(self, pages):
        pages.login_page.open()
        pages.login_page.log_in()

        pages.contracts_page.assert_open()

        pages.requisites_page.open()
        initial_requisites = pages.requisites_page.get_requisites()

        pages.requisites_page.open_edit_sidebar()

        return initial_requisites

    # Проверяем happy path (успешноe заполнение формы)
    @pytest.mark.happy_path
    def test_fill_edit_form_success(self, pages):
        self.setup(pages)

        pages.edit_sidebar.fill_form()
        pages.edit_sidebar.save_form()

        pages.requisites_page.verify_success_popup()
        pages.requisites_page.verify_saved_info()

    # Проверяем ошибки в полях, после чего закрываем форму редактирования
    @pytest.mark.form_errors
    def test_verify_edit_form_errors(self, pages):
        self.setup(pages)

        pages.edit_sidebar.clear_all_fields()
        pages.edit_sidebar.click_save()

        pages.edit_sidebar.verify_field_errors()

        pages.edit_sidebar.click_cancel()
        pages.edit_sidebar.expect_invisible()

    # Проверяем данные после отмены заполнения полей
    @pytest.mark.fill_cancel
    def test_verify_fill_form_cancel(self, pages):
        initial_requisites = self.setup_initial_requisites(pages)

        pages.edit_sidebar.fill_kpp()
        pages.edit_sidebar.fill_address()
        pages.edit_sidebar.click_cancel()

        pages.requisites_page.compare_actual_and_initial_requisites(initial_requisites)

        pages.edit_sidebar.expect_invisible()
