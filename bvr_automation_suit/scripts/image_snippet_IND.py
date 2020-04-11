from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import clipboard
import time
import pickle
from selenium import webdriver
import platform
import os
from xlrd import open_workbook
import json
import requests

data = {}
chromepath = ""

if platform.system() == "Darwin":
    chromepath = os.path.abspath("../drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver")
chrome_options = webdriver.ChromeOptions()
default_sippet ="""<a href="javascript:void(0)"><img border="0" src="https://s3-us-west-2.amazonaws.com/data.bestviewsreviews.com/CATEGORY_IMG/no-image.jpg" ></a>
                <img src="//ir-na.amazon-adsystem.com/e/ir?t=bestviewsre00-20&l=am2&o=1&a=B07KQT4SQJ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />"""
dpl_update_url = "https://dpl.bestviewsreviews.com/api/product/"
headers={'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"}
dpl_fetch_asin_code_url = "https://dpl.bestviewsreviews.com/api/product/no_snippet/IND"

chrome_options.add_argument('--headless')

chrome_options.add_argument("--incognito")

chrome_options.add_argument('--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')

chrome_options.add_argument(f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')

driver = webdriver.Chrome(executable_path=chromepath,chrome_options=chrome_options)

# driver.get("https://affiliate-program.amazon.com/")

driver.get("https://affiliate-program.amazon.in")

time.sleep(0.3)

driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
driver.find_element_by_class_name("a-button-text").click()
time.sleep(0.3)
driver.find_element_by_name("email").send_keys("sidakpreet@shorthillstech.com")
# driver.find_element_by_name("email").send_keys("ranjeeta@parkcircletech.com")
driver.find_element_by_name("password").send_keys("Sidak7Singh")
# driver.find_element_by_name("password").send_keys("ranjeeta123")
driver.find_element_by_id("signInSubmit").click()
time.sleep(0.3)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
def amazon_affiliate(asin):
    # try:
        asin_val = asin
        filename = asin+".json"
        driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(2)
        # data.update(asin_val)
        while 'No results found' in driver.page_source:
            driver.find_element_by_xpath("//*[@placeholder='keyword or ASIN/ISBN']").clear()
            time.sleep(0.3)
            #Add default image snippet
            data1 = {"large_image_snippet":default_sippet,
                    "medium_image_snippet":default_sippet,
                        "small_image_snippet":default_sippet}
            requests.put(url=dpl_update_url + asin_val + "/" + "update", data=data1,
                            headers=headers)
            print("returning")
            return
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
        c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
        c[1].click()
        driver.find_element_by_xpath("//a[@title='Image Only']").click()
        time.sleep(0.3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.2)
        driver.find_elements_by_xpath("//*[@data-action = 'a-dropdown-button']")[2].click()
        time.sleep(0.5)
        drop_down = driver.find_element_by_xpath("//div[@class ='a-popover-inner']")
        image_el = drop_down.find_elements_by_tag_name("li")
        a = 0
        time.sleep(1)
        large = ""
        medium = ""
        small = ""
        for j in image_el:
            j.find_element_by_id("dropdown1_"+str(a)).click()
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();",
                                    driver.find_element_by_id("ac-productlinks-ad-code-panel-image-button-announce"))
            time.sleep(0.3)
            if a==0:
                large = clipboard.paste()
            elif a==1:
                medium = clipboard.paste()
            elif a==2:
                small = clipboard.paste()
            a = a+1
            driver.find_elements_by_xpath("//*[@data-action = 'a-dropdown-button']")[2].click()
            time.sleep(1)
        # product_detail = {
        #     "asin": str(asin_val),
        #     "url": str(url),
        #     "large":str(large),
        #     "medium":str(medium),
        #     "small":str(small)
        # }
        data1 = {"large_image_snippet":large,
                "medium_image_snippet":medium,
                    "small_image_snippet":small}
        requests.put(url=dpl_update_url + asin_val + "/" + "update", data=data1,
                        headers=headers)
        # data.update(product_detail)
        # with open("/Users/aashishsaini/PycharmProjects/bvr_automation_suit/json/"+filename, 'w') as json_file:
        #     json.dump(data, json_file,indent=4)
        print("Done for "+asin_val)
        driver.find_element_by_xpath("//a[@title = 'Home']").click()
    # except:
    #     return
process_flag = True
if str(requests.get(dpl_fetch_asin_code_url, headers=headers).json()["asin"]) is not "":
    while str(requests.get(dpl_fetch_asin_code_url, headers=headers).json()["asin"]) is not "":
        try:
            asin_code = requests.get(dpl_fetch_asin_code_url, headers=headers).json()["asin"]
            print(asin_code)
            amazon_affiliate(asin_code)
        except:
            print("There is some error ...")
            process_flag = False
else:
    print("All products has been already updated, No new or pending product found to update image snippet data")
driver.quit()