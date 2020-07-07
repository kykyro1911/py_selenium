from selenium import webdriver
import time

browser = webdriver.Chrome()
#browser = webdriver.Firefox()
'''
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("selenium")
#通过id = kw定位百度输入框，通过键盘方法send_keys()向输入框中输入selenium。

browser.find_element_by_id("su").click()
#通过id=su定位搜索按钮，并向按钮发送单击事件click()

browser.implicitly_wait(30)
time.sleep(3)
'''

a = browser.find_element_by_class_id("logo_default")
print(a)


browser.quit()
