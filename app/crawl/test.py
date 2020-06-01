from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get('https://passport.weibo.cn/signin/login')
time.sleep(2)
username = 'zhangle231@3g.sina.cn'
password = 'zl87317937'
driver.find_element_by_id("loginName").send_keys(username)
driver.find_element_by_id("loginPassword").send_keys(password)
driver.find_element_by_id("loginAction").click()
time.sleep(5)

es = driver.find_elements_by_xpath("//div[@class='weibo-text']")

driver.implicitly_wait(1)

for i in range(10):
    print('exe script')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        driver.find_elements_by_xpath('//*[@id="waterfall"]/div[2]/div[33]/div/div/a')
    except NoSuchElementException as e:
        print(e)
    time.sleep(3)
print('finish')

#for e in es:

#    print(e.text)

#driver.close()

