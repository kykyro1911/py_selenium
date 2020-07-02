from zentao_login import web_login
from selenium.webdriver.support.ui import Select


def search_bug():
    browser = web_login()
    
    #test_bug
    top_ui = browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]')
    top_ui.click()
    bug_list = browser.find_element_by_xpath('//*[@id="subNavbar"]/ul/li[1]/a')
    bug_list.click()

    #app_model
    drop_menu = browser.find_element_by_id('dropMenu')

    

if __name__ == "__main__":
    search_bug()
