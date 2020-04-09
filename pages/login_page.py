from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Login Url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), "Not Found Log_In Form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Not Found Registration Form"