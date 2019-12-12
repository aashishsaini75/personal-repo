from selenium import webdriver
import csv
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver  = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/dOCTR/web_drivers/chromedriver",chrome_options=chrome_options)
b=0
v=0
m =0
c=0
a=4
url_list1=["http://locate.covd.org/Search/DoSearch?page=1&Country=US&State=NY&PhysicianLastName=&x=81&y=23","http://locate.covd.org/Search/DoSearch?page=2&Country=US&State=NY&PhysicianLastName=&x=81&y=23","http://locate.covd.org/Search/DoSearch?page=3&Country=US&State=NY&PhysicianLastName=&x=81&y=23","http://locate.covd.org/Search/DoSearch?page=4&Country=US&State=NY&PhysicianLastName=&x=81&y=23"]
url_list2=["http://locate.covd.org/Search/DoSearch?page=1&Country=US&State=TX&x=58&y=32","http://locate.covd.org/Search/DoSearch?page=2&Country=US&State=TX&x=58&y=32","http://locate.covd.org/Search/DoSearch?page=3&Country=US&State=TX&x=58&y=32"]
with open('covd_addresses.csv', "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["First Name", "Last Name","Company Name", "Degree", "Address", "City", "State", "ZIP", "Phone Number", "Email",
         "Lat/Long", "URL"])
    for p in range(2):
        for x in range(a):
            if m ==0:
                print("NY SCRAPING")
                driver.get(url_list1[b])
            else:
                print("TX SCRAPING")
                driver.get(url_list2[c])
                c = c + 1
            location_url = driver.find_elements_by_xpath("//*[@class = 'doctor']")
            url_list = []
            for i in location_url:
                url_list.append(i.get_attribute("href"))
            pagination_count = driver.find_elements_by_class_name("page")

            for j in url_list:
                driver.execute_script('window.open("{}","_blank");'.format(j))
                driver.switch_to.window(driver.window_handles[-1])
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID, "doctorInfo")))
                doctor_name_el = driver.find_element_by_id("doctorInfo").find_elements_by_class_name("bold")[0].text
                company_name_el = \
                driver.find_element_by_xpath("//*[@id = 'doctorInfo']").find_elements_by_tag_name("div")[1]
                doctr_update = str(doctor_name_el).split(",")
                doctr_degree = doctr_update[1::]
                doctr_degree0 = str(doctr_degree).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
                doctor_name = doctr_update[0]
                doctor_name_split = str(doctor_name).split(" ")
                first_name = doctor_name_split[0]
                second_name = doctor_name_split[1]
                address = driver.find_element_by_id("Address").text
                citystatezip = driver.find_element_by_id("CityStateZip").text
                adress_split_for_city_state = str(citystatezip).split(",")
                adress_split = str(citystatezip).split(" ")
                city0 = adress_split_for_city_state[0]
                city = str(city0).replace(",", "")
                state0 = adress_split_for_city_state[1]
                state = " ".join(re.findall("[a-zA-Z()]+", state0))
                zip = adress_split[-1]
                phonenumber0 = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID, "PhoneNumber"))).text
                if len(phonenumber0) >= 4:
                    phonenumber = str(phonenumber0).replace("Ph: ", "")
                else:
                    phonenumber = "Not Available"
                time.sleep(1)
                email = driver.find_element_by_id("innerOfficeInfo").find_element_by_xpath(
                    "//a[contains(text(),'@')]").text
                lat_long0 = driver.find_element_by_class_name("mapIt").get_attribute("onclick")
                lat_long1 = str(lat_long0)[12:35]
                lat_long = lat_long1.replace(")", "").replace(";", "")
                company_name = "Not available"
                if len(company_name_el.text) >= 1:
                    company_name = company_name_el.text
                else:
                    pass
                csv_writer.writerow(
                    [first_name, second_name, company_name, doctr_degree0, address, city, state, zip, phonenumber,
                     email, lat_long, j])
                # print("first name "+str(first_name)+"\n","last name "+str(second_name)+"\n","Doctor degree "+str(doctr_degree)+"\n", "address "+str(address)+"\n", "City"+str(city)+"\n" "State"+str(state)+"\n","Zip"+str(zip)+"\n","phone_number "+str(phonenumber)+"\n", "email"+str(email)+"\n","URL"+str(j)+"\n")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("No.of Location= " + str(v))
                v = v + 1
            b = b + 1
        a=a-1
        m = m+1











