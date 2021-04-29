from selenium import webdriver
from datetime import datetime as dt

driverpath = 'chromedriver.exe'
urls = {'login':'https://eclass.sogang.ac.kr/ilos/main/member/login_form.acl'}

userdata = ('20211575', '##########')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--window-size=1280,720')

driver = webdriver.Chrome(driverpath, options=options)

driver.get(urls['login'])

driver.find_element_by_xpath('//input[@id="usr_id"]').send_keys(userdata[0])
driver.find_element_by_xpath('//input[@id="usr_pwd"]').send_keys(userdata[1])
driver.execute_script('loginForm()')


ol = driver.find_elements_by_xpath('//div[@class="index-leftarea02"]/div[@class="m-box2"][1]/ol/li[not(@class) and span]')
D = dict()
for x in ol:
   D[x.find_element_by_xpath('em').text.split()[0]] = x.find_element_by_xpath('span').text.split()
print(D)

driver.quit()
