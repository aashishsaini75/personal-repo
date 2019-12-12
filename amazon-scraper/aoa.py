from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import clipboard
import time
import pickle
from selenium import webdriver

url = "https://www.aoa.org/doctor-locator-search?tab=basic"
driver = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/amazon-scraper/drivers/chromedriver")
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//a[@href = '#advanced']").click()
state_list = driver.find_element_by_id("state").find_elements_by_tag_name("option")
state_list1 = []
for i in state_list:
    state_list1.append(i.get_attribute("value"))
while '' in state_list1:
   state_list1.remove('')

url1 = "https://www.aoa.org/doctor-locator-search/dr-locator-search-results?miles=50&state="
a = 0
for j in range(len(state_list1)):
    driver.get(url1+str(state_list1[a]))
    a=a+1
