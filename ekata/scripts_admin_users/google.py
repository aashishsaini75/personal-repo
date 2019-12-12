from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "https://www.google.com/flights?hl=en"
driver = webdriver.Chrome("..//web_drivers/chromedriver")
driver.get(url)
input = driver.find_elements_by_xpath("//div[@role = 'presentation']")
time.sleep(1)
input[0].click()
driver.find_element_by_xpath("//input[@placeholder ='Where from?']").clear()
driver.find_element_by_xpath("//input[@placeholder ='Where from?']").send_keys("Mumb")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder ='Where from?']").send_keys(Keys.DOWN)
time.sleep(0.5)
driver.find_element_by_xpath("//input[@placeholder ='Where from?']").send_keys(Keys.ENTER)
time.sleep(0.5)
input[1].click()
driver.find_element_by_xpath("//input[@placeholder ='Where to?']").clear()
driver.find_element_by_xpath("//input[@placeholder ='Where to?']").send_keys("bali")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder ='Where to?']").send_keys(Keys.DOWN)
time.sleep(0.5)
driver.find_element_by_xpath("//input[@placeholder ='Where to?']").send_keys(Keys.ENTER)
time.sleep(0.5)
input[2].click()
time.sleep(0.5)
next_date = driver.find_elements_by_xpath("//div[@jstcache='8957']")
for j in range(3):
    next_date[0].click()
for i in range(7):
    next_date[1].click()
driver.find_element_by_xpath("//div[@class = 'eE8hUfzg9Na__overlay']").click()

# from time import sleep
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as ec
# # from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--disable-popup-blocking")
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(executable_path="..//web_drivers/chromedriver",chrome_options=options)
# driver.maximize_window()
# driver.fullscreen_window()
# driver.get('https://www.sonyliv.com/')
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//span[@class="menu-text ng-binding"]').click()
# driver.find_element_by_partial_link_text('SONY TV SHOWS').click()
# sleep(2)
# driver.find_element_by_xpath("//li[@ng-repeat='item in data']").click()
