from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import clipboard
import time
import pickle
from selenium import webdriver
import platform
import os
import requests
from selenium.webdriver.common.keys import Keys

cat_slug = input("Please input the category slug name")
data = {}
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("../drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver")
chrome_options = webdriver.ChromeOptions()
from selenium import webdriver
base_url = "https://www.amazon.com/gp/product/"
get_api_url ="https://bestviewsreviews.com/api/product/"+cat_slug.strip()+"/no_price"
update_api_url = "https://bestviewsreviews.com/api/product/B01BUYJX6G/"+cat_slug.strip()+"/update"
headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"}
driver = webdriver.Chrome(executable_path=chromepath)
chrome_options.add_argument("window-size=1920x1080")
asin_code = requests.get(get_api_url, headers=headers).json()['asin_list']
print(asin_code)
driver.get("https://www.amazon.com/")
time.sleep(1)
driver.find_element_by_id("nav-packard-glow-loc-icon").click()
time.sleep(1)
driver.find_element_by_id("GLUXZipUpdateInput").send_keys("10001")
apply = driver.find_element_by_id("GLUXZipUpdate-announce")
driver.execute_script("arguments[0].click();", apply)
time.sleep(1)
driver.find_element_by_tag_name("body").click()
time.sleep(1)
for i in asin_code:
    driver.get(base_url+str(i))
    update_api_url = "https://bestviewsreviews.com/api/product/"+i+"/" + cat_slug.strip() + "/update"
    if "See price in cart" in driver.page_source:
            time.sleep(0.2)
        # try:
            driver.get("https://www.amazon.com/gp/offer-listing/"+i+"/ref=olp_twister_child?ie=UTF8&mv_style_name=0")

            price = driver.find_element_by_xpath("//span[@class = 'a-size-large a-color-price olpOfferPrice a-text-bold']").text
            data1 = {'price': str(price)
                     }
            res = requests.put(url=update_api_url, data=data1,
                               headers=headers)
            print(res)
            print("done for " + i + "Price is " + price)
        # except:
        #     pass
    elif "Available from" in driver.page_source:
        time.sleep(0.1)
        driver.get("https://www.amazon.com/gp/offer-listing/"+i+"/ref=dp_olp_afts?ie=UTF8&condition=all")
        time.sleep(0.5)
        price = driver.find_element_by_xpath("//span[@class ='a-size-large a-color-price olpOfferPrice a-text-bold']").text
        data1 = {'price': str(price)
                 }
        res = requests.put(url=update_api_url, data=data1,
                           headers=headers)
        print(res)
        print("done for " + i + "Price is " + price)



    try:
        time.sleep(0.5)
        price = driver.find_element_by_xpath("//span[@id ='priceblock_ourprice']").text
        # print(price)
        data1={'price':str(price)
        }
        res = requests.put(url=update_api_url, data=data1,
                     headers=headers)
        print(res)
        print("done for " + i + "Price is " + price)

    except:
        try:
            time.sleep(0.5)
            price = driver.find_element_by_xpath("//span[@id ='price_inside_buybox']").text
            # print(price)
            data1 = {'price': str(price)
                     }
            res = requests.put(url=update_api_url, data=data1,
                         headers=headers)
            print(res)
            print("done for " + i+"Price is "+price)
        except:
            pass

