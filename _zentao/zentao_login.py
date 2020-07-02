from zentao_login import read_cfg
from selenium import webdriver
import time

def main():
    #read_ini
    cfg_data = read_cfg()

    #set_Chrome
    driver = webdriver.Chrome()

    #get_zentao
    driver.get("http://192.168.75.53:3014/zentao")

    #wait_loading
    driver.implicitly_wait(30)

    #key_account
    driver.find_element_by_id("account").send_keys(cfg_data[1])
    driver.find_element_by_name("password").send_keys(cfg_data[2])
    driver.implicitly_wait(30)

    #press_login
    driver.find_element_by_id("submit").click()
    driver.implicitly_wait(30)

    #quit_Chrome
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
