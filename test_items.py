import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exists(browser):
    browser.get(link)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket

