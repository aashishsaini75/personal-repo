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
data['image_src'] = []
filename = ""
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("../drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver_linux")
chrome_options = webdriver.ChromeOptions()
from selenium import webdriver

base_url = "https://www.amazon.com/gp/product/"
book = open_workbook("/Users/aashishsaini/PycharmProjects/bvr_automation_suit/data/Affiliate.xlsx")
sheet = book.sheet_by_index(0)
my_list = []
for row in range(1, 1090): #start from 1, to leave out row 0
    my_list.append(str(sheet.cell(row, 0)).replace("text:","").replace("'","")) #extract from first col
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')
chrome_options.add_argument(f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')
driver = webdriver.Chrome(executable_path=chromepath,chrome_options=chrome_options)
for i in my_list:
    driver.get(base_url+i)
    try:
            link = driver.find_element_by_id("landingImage").get_attribute("src")
            data['image_src'].clear()
            data['image_src'].append(link)
            filename = i+ ".json"
    except:
            pass
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
        print("Link Scraped Successfully")

# with open(filename, 'w') as json_file:
#     json.dump(data, json_file)
#     print("Link Scraped Successfully")