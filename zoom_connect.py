from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import schedule
from datetime import datetime

driverpath = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging", "disable-default-apps"])
options.add_argument('--window-size=1280,720')

driver = webdriver.Chrome(driverpath, options=options)

room = ['82365917367', '4326']
driver.get('https://sogang-ac-kr.zoom.us/j/%s#success' %room[0])
driver.find_element_by_xpath('//h3[@role="presentation"][2]/a').click()

# recapcha problem!
