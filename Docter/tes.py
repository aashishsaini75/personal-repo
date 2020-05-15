from selenium import webdriver
import csv
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/dOCTR/web_drivers/chromedriver",chrome_options=chrome_options)
main_url = "https://locate.covd.org/Search/Detailed?profileId=999A5CF2-3911-49D4-807A-186F4B3052D8&markerId=0&lat=52.8450521&lng=-110.8328022&address=20%202802%2015th%20avenue%20Wainwright%2C%20Alberta%20T9W%200A4&Country=CA&State=AB&x=62&y=26"
driver.get(main_url)
address0 = driver.find_element_by_id("CityStateZip").text
address = address0.split(" ")
print(str(address[-2::]).replace("[","").replace("]","").replace("'","").replace(",",""))


