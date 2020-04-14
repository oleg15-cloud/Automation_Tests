from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM), \
        "Basket page has product"


    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_EMPTY_BASKET), \
        "Not found message about empty basket"