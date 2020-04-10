from .pages.product_page import ProductPage
import time

# pytest -v --tb=line --language=en test_product_page.py

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.alert_math_finction()
    page.should_be_after_add_product_in_basket()