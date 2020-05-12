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
base_url = "https://www.amazon.com/gp/product/"
get_api_url ="https://bestviewsreviews.com/api/product/"+cat_slug.strip()+"/no_price"
headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"}
driver = webdriver.Chrome(executable_path=chromepath)
chrome_options.add_argument("window-size=1920x1080")
asin_code = requests.get(get_api_url, headers=headers).json()['asin_list']
print(asin_code)
for i in asin_code:
    driver.get(base_url+str(i))
