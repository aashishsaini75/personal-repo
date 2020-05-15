from selenium import webdriver
import pymsteams
import time
import csv
import requests
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/b3a5e626-8dd4-4987-9e58-7dab05972f37@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/a8546ebb7c074509b16ba5cd6ded79b8/47631de8-81c9-4b66-8cc3-1290c874fdf4")
# myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/70f03e61-7587-4e07-b4b7-7fc89e589cf5@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/6640fc79c06b42a7b09330803add3e39/21bde621-fde7-4e25-8007-bb1ded8aad73")
data1 = {"active":False}
dpl_update_url = "https://dpl.bestviewsreviews.com/api/product/"
prod_update_url = "https://bestviewsreviews.com/api/product/"
dev_update_url = "https://dev1.bestviewsreviews.com/api/product/"
dev_url = "https://dev1.bestviewsreviews.com/all/"
prod_url = "https://bestviewsreviews.com/all/"
base_url = "https://www.amazon.com/gp/product/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
print("Waiting to load all category page...")
driver.get(prod_url)
driver.maximize_window()
cat_count = 0
cat_links = []
cat = driver.find_elements_by_xpath("//li[@class ='ham-items']")
for i in cat:
   slug_el = str(i.get_attribute("onclick")).split("=")
   slug = slug_el[1].replace("'","")
   # print(slug)
   cat_links.append("https://bestviewsreviews.com"+slug.strip())

for j in cat_links:
    print("Waiting to load category page..."+str(j)+"\n"+("Category number is "+ str(cat_count)))
    print("--------------------------------------------------------------")
    driver.get(j)
    cat_count = cat_count+1
    time.sleep(0.5)
    if '<button type="button" class="btn btn-primary" name="see_more_button" id="see_more_button" style="display: none;">See More Products</button>' not in driver.page_source:
        while '<button type="button" class="btn btn-primary" name="see_more_button" id="see_more_button" style="display: none;">See More Products</button>' not in driver.page_source:
            time.sleep(1)
            driver.find_element_by_id("see_more_button").click()
            print("Loading all products...")
    else:
        pass
    buttons = driver.find_elements_by_xpath("//div[@class ='buy-now-compare']//button[@class ='btn btn-primary']")
    for k  in buttons:
        k.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)
        asin_code = str(driver.current_url).split("/")[-2]
        if "The requested resource was not found on this server." in driver.page_source:
            res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
            if res2.text == '{"success":"update successfull"}':
                print(str(asin_code) + " Product Disabled Successfully \n Reason: The requested resource was not found on this server.\n Manually test on : "+ base_url+asin_code)
            else:
                print("API Update error, Error Code: "+str(res2.text))

        elif "We don't know when or if this item will be back in stock." in driver.page_source:

            res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
            if res2.text == '{"success":"update successfull"}':
                print(str(asin_code) + " Product Disabled Successfully \n Reason: We don't know when or if this item will be back in stock.\n Manually test on : "+ base_url+asin_code)
            else:
                print("API Update error, Error Code: "+str(res2.text))


        elif "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." in driver.page_source:

            res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
            if res2.text == '{"success":"update successfull"}':
                print(str(asin_code) + " Product Disabled Successfully \n Reason: Sorry! We couldn't find that page. Try searching or go to Amazon's home page.\n Manually test on : "+ base_url+asin_code)
            else:
                print("API Update error, Error Code: "+str(res2.text))


        elif "No Product matches the given query." in driver.page_source:

            res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
            if res2.text == '{"success":"update successfull"}':
                print(str(asin_code) + " Product Disabled Successfully \n Reason: No Product matches the given query.\n Manually test on : "+ base_url+asin_code)
            else:
                print("API Update error, Error Code: "+str(res2.text))

        else:
            print(str(asin_code) + " Product is available to sale\n Manually test on : "+ base_url+asin_code)
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("--------------------------------------------------------------")