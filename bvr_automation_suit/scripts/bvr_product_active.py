import requests
import json
from selenium import webdriver
import pymsteams
import time
import csv
import requests
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
data1 = {"active":True}
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/b3a5e626-8dd4-4987-9e58-7dab05972f37@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/a8546ebb7c074509b16ba5cd6ded79b8/47631de8-81c9-4b66-8cc3-1290c874fdf4")
base_url = "https://www.amazon.com/gp/product/"
prod_url = "https://bestviewsreviews.com/api/product/inactive_list"
prod_update_url = "https://bestviewsreviews.com/api/product/"
res = requests.get(url=prod_url,headers = {'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
data = json.loads(res.text)
asin_list = []
for i in data:
    asin_list.append(i["asin_code"])
for k in asin_list:
    driver.get(base_url+k)
    time.sleep(0.3)
    if "We don't know when or if this item will be back in stock." not in driver.page_source:
        res = requests.put(url=prod_update_url + k + "/" + "update", data=data1,
                           headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})

        print(str(k) + " Product enabled Successfully \n Manually test on : "+ base_url+k)
    else:
        print("No Action Required")
    if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." in driver.page_source:
        res = requests.put(url=prod_update_url + k + "/" + "update", data={"active":False},
                           headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
        print("Oh! Product is Removed from amazon, Disabled the product again \n Manually test on : "+ base_url+k)
    else:
        pass
driver.quit()
