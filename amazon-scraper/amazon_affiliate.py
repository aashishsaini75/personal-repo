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
data = {}
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver_linux")
chrome_options = webdriver.ChromeOptions()
from selenium import webdriver

book = open_workbook("/Users/aashishsaini/PycharmProjects/amazon-scraper/excel_data/Aashish(ASIN).xlsx")
sheet = book.sheet_by_index(0)
my_list = []
for row in range(19, 20): #start from 1, to leave out row 0
    my_list.append(str(sheet.cell(row, 0)).replace("text:","").replace("'","")) #extract from first col

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')
chrome_options.add_argument(f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')
driver = webdriver.Chrome(executable_path=chromepath,chrome_options=chrome_options)
driver.get("https://affiliate-program.amazon.com/")
time.sleep(0.3)
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
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))

def amazon_affiliate():
    try:
        for i in my_list:
            asin_val = i
            filename = i+".json"
            driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
            time.sleep(0.3)
            driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(2)
            # data.update(asin_val)
            while "No results found" in driver.page_source:
                driver.find_element_by_xpath("//*[@placeholder='keyword or ASIN/ISBN']").clear()
                time.sleep(0.3)
                return
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
            c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
            c[1].click()

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@title ='Text Only']")))
            driver.find_element_by_xpath("//*[@title ='Text Only']").click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")))
            link = driver.find_element_by_xpath("//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")
            driver.execute_script("arguments[0].click();", link)
            time.sleep(0.3)
            for i in range(5):
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, "//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']")))
                driver.find_element_by_xpath("//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']").click()
            url = clipboard.paste()
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
            product_detail = {
                "asin": str(asin_val),
                "url": str(url),
                "large":str(large),
                "medium":str(medium),
                "small":str(small)
            }
            data.update(product_detail)
            with open(filename, 'w') as json_file:
                json.dump(data, json_file,indent=4)
            print("scraped of "+asin_val)
            driver.find_element_by_xpath("//a[@title = 'Home']").click()
    except:
        return
amazon_affiliate()
