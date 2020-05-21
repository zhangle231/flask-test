from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://passport.weibo.cn/signin/login')
time.sleep(5)
username = 'zhangle231@3g.sina.cn'
password = 'zl87317937'
driver.find_element_by_id("loginName").send_keys(username)
driver.find_element_by_id("loginPassword").send_keys(password)
driver.find_element_by_id("loginAction").click()
time.sleep(8)
driver.close()

