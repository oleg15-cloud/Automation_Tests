from selenium.webdriver.common.by import By
import time

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOG_IN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")
    INPUT_REGISTER_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    INPUT_REGISTER_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    INPUT_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='registration-password2']")
    BTN_REGISTER = (By.XPATH, "//button[@name='registration_submit']")
    EMAIL = str(time.time()) + "@fakemail.org"
    PASSWORD = str(time.time()) + "@fakemail.org"

class ProductPageLocators():
    PRICE_ON_PAGE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[2]")
    PRODUCT_NAME_ON_PAGE = (By.XPATH, "//h1")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//div[1]/div/strong")
    BTN_ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")


class BasketPageLocators():
    MESSAGE_IN_EMPTY_BASKET = (By.XPATH, '//div/p')
    PRODUCT_FORM = (By.XPATH, "//form[@class='basket_summary']")