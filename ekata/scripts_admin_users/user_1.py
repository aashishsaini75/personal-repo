import csv
import unittest
import random
from selenium import webdriver
url = "http://52.10.58.58:88/register/"
driver = webdriver.Chrome("/Users/aashishsaini/PycharmProjects/ekata/web_drivers/chromedriver")
val = random.randint(0,9999999)
username = "bot_user_1_"+str(val)
email="bot_user_1@gmail.com"
driver.get(url)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password1").send_keys("bot_user_1_password")
driver.find_element_by_name("password2").send_keys("bot_user_1_password")
driver.find_element_by_xpath("//*[@class = 'btn btn-outline-info']").click()
with open('ekata_user_sheet.csv', "a") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([username,email])
driver.close()


