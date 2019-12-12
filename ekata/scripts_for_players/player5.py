import unittest
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
val = random.randint(0,9999999)
player_username = "bot_player_5_"+str(val)
email = "bot_player_5@gmail.com"
url = "http://52.10.58.58:88/"
driver = webdriver.Chrome("/Users/aashishsaini/PycharmProjects/ekata/web_drivers/chromedriver")
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//*[@href = '/login/']").click()
driver.find_element_by_name("username").send_keys("bot_user_5_5635095")
driver.find_element_by_name("password").send_keys("bot_user_5_password")
driver.find_element_by_xpath("//*[@class = 'btn btn-outline-info']").click()
a=5
for i in range(5):
    val = random.randint(0, 9999999)
    player_username = "bot_player_"+str(a)+"_"+str(val)
    email = "bot_player_"+str(a)+"@gmail.com"
    driver.find_element_by_xpath("//*[@href = '/player/']").click()
    driver.find_element_by_name("name").send_keys(player_username)
    driver.find_element_by_name("valid_business_email").send_keys(email)
    driver.find_element_by_id("player-submit-btn").click()
    with open('ekata_player_sheet.csv', "a") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([player_username, email])
    a = a+1
# driver.find_element_by_id("newGameBtn").click()
# driver.find_element_by_id("tutPgStartGameBtn").click()
# time.sleep(2)
# click = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@class ='tpbl-circle good-circle grow-animation-good']")))
# for i in range(10):
#     time.sleep(1)
#     click.click()
