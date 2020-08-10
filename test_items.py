link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_basket(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
