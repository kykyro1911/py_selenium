"""from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com/")



driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("btnK").click()

driver.implicitly_wait(30)
sleep(3)

driver.quit()"""

'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()

driver.implicitly_wait(30)
time.sleep(3)


driver.quit()
'''
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")
driver.maximize_window()


# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).context_click()
