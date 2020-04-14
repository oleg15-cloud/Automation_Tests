from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def alert_math_function(self):
        self.solve_quiz_and_get_code()

    def should_be_after_add_product_in_basket(self):
        self.check_message_about_product_in_baskect()
        self.check_product_price_in_message()

    def check_message_about_product_in_baskect(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        assert message == f"{product_name} has been added to your basket.", \
            "Not Found Message or Incorrect Product Name In Message"

    def check_product_price_in_message(self):
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE).text
        assert product_price_in_message == product_price, \
            "Incorrect Product Price"

    def should_not_be_message_after_add_product_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def succes_message_should_be_disappeared(self):
        assert  self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message was not disappeared"