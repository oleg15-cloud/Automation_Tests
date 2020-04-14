import time
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.FORM_REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FORM_REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FORM_REG_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REG).click()


    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Login Url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), "Not Found Log_In Form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Not Found Registration Form"