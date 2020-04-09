import time
import pytest


def test_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button != None, "Button not found"