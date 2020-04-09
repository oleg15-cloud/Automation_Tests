import time
import pytest
from .pages.main_page import MainPage


def test_language(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()