import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    #time.sleep(30)
    try:
       browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    except:
       print ("Don't find button")
       assert False