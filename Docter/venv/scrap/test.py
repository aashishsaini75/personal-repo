from selenium import webdriver
import csv
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
pro_url = "https://www.amazon.com/Ticwatch-Smartwatch-Swim-Ready-Connectivity-Available/dp/B07RKQBHC9/ref=cm_cr_arp_d_product_top?ie=UTF8"
# url = "https://locate.covd.org/Search/Detailed?profileId=0A43C4F7-A32B-4485-911C-3F543B400A3D&markerId=0&lat=33.307757&lng=-111.858661&address=916%20W%20%20Chandler%20Blvd%20%231%20Chandler%2C%20AZ%2085225&Country=US&State=AZ&x=48&y=23"
driver = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/dOCTR/web_drivers/chromedriver")
driver.get(url)
driver.find_element_by_id("ap_email").send_keys("aashishsaini75@gmail.com")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Helloone1@")
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_id("ap_password").send_keys("Helloone1@")
time.sleep(16)
driver.get(pro_url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
data = driver.find_element_by_xpath("//div[@cel_widget_id ='desktop-rhf_widget_pop_multi_srecs_sabr']").find_element_by_tag_name("div").get_attribute("data-a-carousel-options")
print(data)
