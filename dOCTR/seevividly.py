from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import time
import random
import string
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

''''''''''''''''''''''''''''''''''''''''''''
extensions = ['com', 'net', 'org', 'gov']
domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']
winext = extensions[random.randint(0, len(extensions) - 1)]
windom = domains[random.randint(0, len(domains) - 1)]
acclen = random.randint(10,15)
winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))
finale = winacc + "@" + windom + "." + winext
''''''''''''''''''''''''''''''''''''''''''''

url = "https://www.seevividly.com/doctor_locator"
driver = webdriver.Chrome(executable_path="..//dOCTR/web_drivers/chromedriver",chrome_options=chrome_options)
driver.get(url)
driver.find_element_by_id("input-name").send_keys(winacc)
driver.find_element_by_id("input-email").send_keys(finale)
driver.find_element_by_xpath("//*[@placeholder = 'Address, city, or zipcode*']").send_keys("New York")
time.sleep(1)
driver.find_element_by_xpath("//*[@id = 'autocomplete']").send_keys(Keys.DOWN)
time.sleep(1)
driver.find_element_by_xpath("//*[@id = 'autocomplete']").send_keys(Keys.ENTER)
driver.find_element_by_id("input-consent").click()
time.sleep(1)
driver.find_element_by_id("find_my_provider_button").click()
location = driver.find_elements_by_xpath("//*[@class = 'bold fs-15']")
loc_url_list = []
not_available = "N/A"
with open('seevividly.csv', "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["Company Name", "Salutation","First Name", "Last Name", "Degree Designation", "Job Title", "Email Address", "Website", "Office Phone", "Number of Locations",
         "City", "State","County (ZIP)","Address","URL (For Verification)",])
    for i in location:
        loc_url_list = i.get_attribute("href")
        company_name = i.text
        driver.execute_script('window.open("{}","_blank");'.format(loc_url_list))
        driver.switch_to.window(driver.window_handles[-1])
        address_el = driver.find_elements_by_xpath("//span[@class= 'block']")
        address = address_el[0]
        address0 = address.text
        address1 = str(address0).replace("Address:", "")
        split_address = address1.split(",")
        office_phone0 = address_el[2].find_element_by_tag_name("a").text
        # data = [company_name,]
        address_1 = ""
        if address1 == " Visit Project LUMA":
            address_1 = not_available
        else:
            address_1= address1
        zip = ""
        if address_1 == not_available:
            zip = not_available
        else:
            zip = address0[-6:]
        office_phone = not_available
        if len(office_phone0) <=1:
            office_phone = not_available
        else:
            office_phone = office_phone0
        first_name = not_available
        last_name = not_available
        salutation = not_available
        degree_desigination = not_available
        job_title = not_available
        email_address = not_available
        url = loc_url_list
        no_of_location = not_available
        state0= str(address0[-9:-5]).replace(",","").strip()
        if len(state0) <= 1:
            state = not_available
        else:
             state = str(state0).strip()
        address_for_city = str(address1.replace("\n"," "))
        city0 = address_for_city.strip().split(" ")
        city1 = str(city0[-3]).replace(",","").strip()
        city = ""
        if city1 == "Visit":
            city = not_available
        else:
            city = str(city1).strip()
        if city1 == "York":
            city = "New York"
        else:pass
        final_address0 = str(city0[:-3]).replace("[","").replace("]",'').replace(",","").replace("'","")
        final_address = ""
        if len(final_address0) <= 1:
            final_address = not_available
        else:
             final_address = str(final_address0).strip()
        website = (address_el[1].find_element_by_tag_name("a").get_attribute("href"))
        data = [company_name,salutation,first_name,last_name,degree_desigination,job_title,email_address,website,office_phone,office_phone,city,state,zip,final_address,url]
        print(data)
        csv_writer.writerow(data)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])










