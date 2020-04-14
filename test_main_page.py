import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)    # Создаем объект новой страницы, + помещаем туда url
        login_page.should_be_login_page()                       # Проверяем страницу на которую перешли


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_text_about_empty_basket()