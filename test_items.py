import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_browser_language_basket_btn(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button.is_displayed(), "Button is not displayed"
