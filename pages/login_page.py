from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url,'uncorrect url'

    def should_be_login_form(self):
        list_res = self.browser.find_elements(*LoginPageLocators.FORM_REGISTRATION)
        assert len(list_res)==1,'should be login form'

    def should_be_register_form(self):
        list_res = self.browser.find_elements(*LoginPageLocators.FORM_LOGIN)
        assert len(list_res)==1,'should be register form'