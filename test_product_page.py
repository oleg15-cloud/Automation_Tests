from .pages.product_page import ProductPage
import pytest
import time
# pytest -v --tb=line --language=en test_product_page.py

@pytest.mark.parametrize('path', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8", "9"])
def test_guest_can_add_product_to_basket(browser, path):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{path}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.alert_math_finction()
    page.should_be_after_add_product_in_basket()