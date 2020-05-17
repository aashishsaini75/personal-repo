from selenium import webdriver
import pymsteams
import time
import csv
import requests

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)

driver.get("https://www.bobcat.com/loaders/compact-track-loaders/models/t550/specs-options")
driver.refresh()
time.sleep(10)
print(driver.page_source)
print(driver.find_element_by_xpath("//span[@title ='ENGINECOOLING--LIQUID']").text)
driver.quit()