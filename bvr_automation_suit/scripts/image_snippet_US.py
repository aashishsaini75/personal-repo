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
default_sippet = '<a target="_blank"  href="https://www.amazon.com/gp/product/B0002OKFA4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0002OKFA4&linkCode=as2&tag=bestviewsre0e-20&linkId=a2dcf944f9b84de2e19f610afa91b6c5"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0002OKFA4&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL110_&tag=bestviewsre0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=bestviewsre0e-20&l=am2&o=1&a=B0002OKFA4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
dpl_update_url = "https://dpl.bestviewsreviews.com/api/product/"
headers = {'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"}
dpl_fetch_asin_code_url = "https://dpl.bestviewsreviews.com/api/product/asin_list/"+cat_slug.strip()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument(
    '--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')
chrome_options.add_argument(
    f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')
driver = webdriver.Chrome(executable_path=chromepath, chrome_options=chrome_options)
driver.get("https://affiliate-program.amazon.com/")
time.sleep(0.3)
driver.maximize_window()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
driver.find_element_by_class_name("a-button-text").click()
time.sleep(0.3)
# driver.find_element_by_name("email").send_keys("info@parkcircletech.com")
driver.find_element_by_name("email").send_keys("ranjeeta@parkcircletech.com")
# driver.find_element_by_name("password").send_keys("Parkcircle123")
driver.find_element_by_name("password").send_keys("ranjeeta123")
driver.find_element_by_id("signInSubmit").click()
time.sleep(0.3)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
def amazon_affiliate(asin):

    # try:
    asin_val = asin
    filename = asin+".json"
    driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(2)
    # data.update(asin_val)
    while 'No results found' in driver.page_source:
        driver.find_element_by_xpath("//*[@placeholder='keyword or ASIN/ISBN']").clear()
        time.sleep(0.3)
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
    try:
        c[1].click()
    except:
        driver.execute_script("arguments[0].click()", c[1])
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
        time.sleep(1)
        driver.execute_script("arguments[0].click();",
                                driver.find_element_by_id("ac-productlinks-ad-code-panel-image-button-announce"))
        time.sleep(1)
        if a==0:
            large = clipboard.paste()
        elif a==1:
            medium = clipboard.paste()
        elif a==2:
            small = clipboard.paste()
        a = a+1
        driver.find_elements_by_xpath("//*[@data-action = 'a-dropdown-button']")[2].click()
        time.sleep(1)
    final_large =("https:"+large.split("<")[2].replace('img border="0" src="',"").replace('"',"").replace(">",""))
    final_medium=("https:"+medium.split("<")[2].replace('img border="0" src="',"").replace('"',"").replace(">",""))
    final_small=("https:"+small.split("<")[2].replace('img border="0" src="',"").replace('"',"").replace(">",""))

    data1 = {"large_image_snippet":final_large,
            "medium_image_snippet":final_medium,
                "small_image_snippet":final_small}

    requests.put(url=dpl_update_url + asin_val + "/" + "update", data=data1,
                    headers=headers)
    print("Done for "+asin_val)
    driver.find_element_by_xpath("//a[@title = 'Home']").click()


# except:
#     return


# try:
asin_code = requests.get(dpl_fetch_asin_code_url, headers=headers).json()
for i in asin_code:
        # print(i)
    amazon_affiliate(i)
# except:
#     print("There is some error ...")



driver.quit()