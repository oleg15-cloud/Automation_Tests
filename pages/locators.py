from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOG_IN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")