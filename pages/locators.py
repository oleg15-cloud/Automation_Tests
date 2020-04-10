from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOG_IN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    PRICE_ON_PAGE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
    PRODUCT_NAME_ON_PAGE = (By.XPATH, "//h1")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//div[1]/div/strong")
    BTN_ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")