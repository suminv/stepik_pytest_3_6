import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements_by_css_selector("#add_to_basket_form")) > 0, "корзинка не найдена"