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
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
data1 = {"active":True}
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/b3a5e626-8dd4-4987-9e58-7dab05972f37@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/a8546ebb7c074509b16ba5cd6ded79b8/47631de8-81c9-4b66-8cc3-1290c874fdf4")
# myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/70f03e61-7587-4e07-b4b7-7fc89e589cf5@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/6640fc79c06b42a7b09330803add3e39/21bde621-fde7-4e25-8007-bb1ded8aad73")
base_url = "https://www.amazon.com/gp/product/"
# dev_url = "http://dev1.bestviewsreviews.com/api/product/inactive_list"
# dpl_url = "http://dpl.bestviewsreviews.com/api/product/inactive_list"
prod_url = "https://bestviewsreviews.com/api/product/inactive_list"
prod_update_url = "https://bestviewsreviews.com/api/product/"
# dev_update_url = "https://dev1.bestviewsreviews.com/api/product/"
# dpl_update_url = "https://dpl.bestviewsreviews.com/api/product/"
res = requests.get(url=prod_url,headers = {'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
data = json.loads(res.text)
# print(data)
asin_list = []
for i in data:
    asin_list.append(i["asin_code"])
for k in asin_list:
    driver.get(base_url+k)
    if "We don't know when or if this item will be back in stock." not in driver.page_source:
        # now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # # create the section
        # myMessageSection = pymsteams.cardsection()
        # # Section Title
        # myMessageSection.title("📢 INFORMATION ⚠️")
        # # Activity Elements
        # myMessageSection.activityTitle("BACK IN STOCK")
        # myMessageSection.activityText("The following category's product is Back in stock at Amazon.com and is now active on Best Views Reviews.")
        # # Facts are key value pairs displayed in a list.
        # # myMessageSection.addFact("Category: ", cat_name)
        # myMessageSection.addFact("ASIN Code: ", k)
        # # myMessageSection.addFact("Product title", title)
        # # myMessageSection.addFact("Product URL", product_url)
        # myMessageSection.addFact("Date & Time", dt_string)
        # # Section Text
        # myMessageSection.text("Product Details")
        # # Section Images
        # myTeamsMessage.summary("summary")
        # # Add your section to the connector card object before sending
        # myTeamsMessage.addSection(myMessageSection)
        # myTeamsMessage.send()
        # requests.put(url=dev_update_url + k + "/" + "update", data=data1,
        #              headers={'Authorization': "Token f099e89c7ccbe3a1a742a7a93cd1a0f2c1b30b33"})
        # requests.put(url=dpl_update_url + k + "/" + "update", data=data1,
        #              headers={'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"})
        res = requests.put(url=prod_update_url + k + "/" + "update", data=data1,
                           headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
        print(str(k) + " Product Updated Successfully ")
    elif "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." not in driver.page_source:
        res = requests.put(url=prod_update_url + k + "/" + "update", data=data1,
                           headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
        print(str(k) + " Product Updated Successfully ")
driver.quit()
