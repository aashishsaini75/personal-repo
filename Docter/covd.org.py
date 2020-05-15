from selenium import webdriver
import csv
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/dOCTR/web_drivers/chromedriver",chrome_options=chrome_options)
main_url = "https://locate.covd.org/"
driver.get(main_url)
driver.maximize_window()
not_available = 'N/A'
time.sleep(2)
county_index_count = 1
county_list_counter = 1
county_el = driver.find_element_by_id("Country").find_elements_by_tag_name("option")
county_list= []
for ab in county_el:
    county_list.append(ab.text)
with open('covd.org.csv', "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["Company Name", "Salutation","First Name", "Last Name", "Degree Designation", "Job Title", "Email Address", "Website", "Office Phone", "Number of Locations",
         "City", "State","County (ZIP)","County","Address","URL (For Verification)","No of location in current state"])
    for n in range(len(county_el)-1):
        driver.get(main_url)
        time.sleep(2)
        county = county_list[county_list_counter]
        county_list_counter = county_list_counter+1
        county_el = driver.find_element_by_id("Country").find_elements_by_tag_name("option")
        county_el[county_index_count].click()
        time.sleep(2)
        state_el = driver.find_element_by_id("State").find_elements_by_tag_name("option")
        state_index_count = 1
        for w in range(int(len(state_el)-1)):
            time.sleep(0.5)
            state_el = driver.find_element_by_id("State").find_elements_by_tag_name("option")
            state_el[state_index_count].click()
            driver.find_element_by_xpath("//*[@value = 'Search']").click()
            location_url = driver.find_elements_by_xpath("//*[@class = 'doctor']")
            no_of_location_in_this_state = driver.find_element_by_xpath("//span[@class = 'results']").text
            pages = driver.find_elements_by_xpath("//a[@class= 'page']")
            pages_count = len(pages)
            loop_count = int(pages_count/2)
            pages_el_contain_count = driver.find_element_by_xpath("//div[@class='pages']").find_elements_by_tag_name("a")
            url_list = []
            for k in location_url:
                url_list.append(k.get_attribute("href"))
            if len(pages_el_contain_count)>=1:
                b = 0
                for p in range(loop_count+1):
                    if b > 0:
                        next_el = driver.find_element_by_xpath("//div[@class='pages']").find_element_by_xpath(
                            "//a[contains (text(),'>>')]")
                        driver.execute_script("arguments[0].click();", next_el)
                        location_url = driver.find_elements_by_xpath("//*[@class = 'doctor']")
                        url_list = []
                        for k in location_url:
                            url_list.append(k.get_attribute("href"))
                    b = b + 1
                    for j in url_list:
                        driver.execute_script('window.open("{}","_blank");'.format(j))
                        driver.switch_to.window(driver.window_handles[-1])
                        WebDriverWait(driver, 20).until(
                            EC.visibility_of_element_located((By.ID, "doctorInfo")))
                        doctor_name_el = driver.find_element_by_id("doctorInfo").find_elements_by_class_name("bold")[
                            0].text
                        company_name_el = \
                            driver.find_element_by_xpath("//*[@id = 'doctorInfo']").find_elements_by_tag_name("div")[1]
                        office_len = driver.find_elements_by_xpath("//*[@class ='officeInfo']")
                        no_of_location = len(office_len)
                        doctr_update = str(doctor_name_el).split(",")
                        doctr_degree = doctr_update[1::]
                        degree_desigination = str(doctr_degree).replace("[", "").replace("]", "").replace("'",
                                                                                                          "").replace(
                            " ",
                            "").replace(
                            ",", ", ")
                        doctor_name = doctr_update[0]
                        doctor_name_split = str(doctor_name).split(" ")
                        first_name = doctor_name_split[0]
                        last_name = doctor_name_split[1]
                        office_info_el = driver.find_elements_by_xpath("//div[@class = 'officeInfo']")
                        xy = 0
                        for ip in range(len(office_info_el)):
                            office_info = office_info_el[xy]
                            final_address0 = office_info.find_element_by_id("Address").text
                            if len(final_address0) >= 1:
                                final_address = final_address0
                            else:
                                final_address = not_available
                            citystatezip = office_info.find_element_by_id("CityStateZip").text
                            adress_split_for_city_state = str(citystatezip).split(",")
                            adress_split = str(citystatezip).split(" ")
                            city0 = adress_split_for_city_state[0]
                            city = str(city0).replace(",", "").replace("Labrador", "Newfoundland and Labrador").replace(
                                "Scotia", "Nova Scotia")
                            country = str(county).strip()
                            if country == "Canada":
                                state_for_canada = office_info.find_element_by_id("CityStateZip").text
                                state_for_canada_final = state_for_canada.split(" ")
                                state_pr = state_for_canada_final[-3]
                                state = str(state_pr).replace("Columbia", "British Columbia").replace(",", "")
                            else:
                                state0 = adress_split_for_city_state[1]
                                state = " ".join(re.findall("[a-zA-Z()]+", state0))
                            if country == "Canada":
                                zip_for_canada = office_info.find_element_by_id("CityStateZip").text
                                zip_for_canada_final = state_for_canada.split(" ")
                                zip = str(zip_for_canada_final[-2::]).replace("[", "").replace("]", "").replace("'",
                                                                                                                "").replace(
                                    ",", "")
                            else:
                                zip0 = adress_split[-1]
                                zip = " ".join(re.findall("[0-9()]+", zip0)).strip().replace(" ", "-")
                            if len(zip) >= 1:
                                zip_final = zip
                            else:
                                zip_final = not_available
                            phonenumber0 = office_info.find_element_by_id("PhoneNumber").text
                            if len(phonenumber0) >= 4:
                                office_phone = str(phonenumber0).replace("Ph: ", "")
                            else:
                                office_phone = not_available
                            email_address = office_info.find_element_by_id("innerOfficeInfo").find_element_by_tag_name(
                                "a").text
                            email = str(email_address).replace("info@covd.org", not_available)
                            lat_long0 = office_info.find_element_by_class_name("mapIt").get_attribute("onclick")
                            lat_long1 = str(lat_long0)[12:35]
                            lat_long = lat_long1.replace(")", "").replace(";", "")
                            company_name = not_available
                            job_el = driver.find_element_by_id("doctorInfo").find_elements_by_tag_name("div")
                            job_title0 = job_el[2].text
                            job_title = str(job_title0).replace("Type: ", "").strip()
                            website_el = office_info.find_element_by_id("WebSite").text
                            if len(email) >= 1:
                                email = email_address
                            else:
                                email = not_available
                            if len(website_el) >= 4:
                                website = str(website_el)
                            else:
                                website = not_available
                            salutation = not_available
                            url = j
                            if len(company_name_el.text) >= 1:
                                company_name = company_name_el.text
                            else:
                                pass
                            data = [company_name, salutation, first_name, last_name, degree_desigination, job_title,
                                    email,
                                    website,
                                    office_phone, no_of_location, city, state, zip_final, county, final_address, url,
                                    no_of_location_in_this_state]

                            csv_writer.writerow(data)
                            xy = xy + 1
                            print(data)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
            else:
                for j in url_list:
                    driver.execute_script('window.open("{}","_blank");'.format(j))
                    driver.switch_to.window(driver.window_handles[-1])
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located((By.ID, "doctorInfo")))
                    doctor_name_el = driver.find_element_by_id("doctorInfo").find_elements_by_class_name("bold")[
                        0].text
                    company_name_el = \
                        driver.find_element_by_xpath("//*[@id = 'doctorInfo']").find_elements_by_tag_name("div")[1]
                    office_len = driver.find_elements_by_xpath("//*[@class ='officeInfo']")
                    no_of_location = len(office_len)
                    doctr_update = str(doctor_name_el).split(",")
                    doctr_degree = doctr_update[1::]
                    degree_desigination = str(doctr_degree).replace("[", "").replace("]", "").replace("'",
                                                                                                      "").replace(
                        " ",
                        "").replace(
                        ",", ", ")
                    doctor_name = doctr_update[0]
                    doctor_name_split = str(doctor_name).split(" ")
                    first_name = doctor_name_split[0]
                    last_name = doctor_name_split[1]
                    office_info_el = driver.find_elements_by_xpath("//div[@class = 'officeInfo']")
                    xy = 0
                    for ip in range(len(office_info_el)):
                        office_info = office_info_el[xy]
                        final_address0 = office_info.find_element_by_id("Address").text
                        if len(final_address0) >= 1:
                            final_address = final_address0
                        else:
                            final_address = not_available
                        citystatezip = office_info.find_element_by_id("CityStateZip").text
                        adress_split_for_city_state = str(citystatezip).split(",")
                        adress_split = str(citystatezip).split(" ")
                        city0 = adress_split_for_city_state[0]
                        city = str(city0).replace(",", "").replace("Labrador", "Newfoundland and Labrador").replace("Scotia", "Nova Scotia")
                        country = str(county).strip()
                        if country == "Canada":
                            print("Yes for state")
                            state_for_canada = office_info.find_element_by_id("CityStateZip").text
                            state_for_canada_final = state_for_canada.split(" ")
                            state_pr = state_for_canada_final[-3]
                            state = str(state_pr).replace("Columbia", "British Columbia").replace(",", "")

                        else:
                            state0 = adress_split_for_city_state[1]
                            state = " ".join(re.findall("[a-zA-Z()]+", state0))
                        if country == "Canada":
                            print("Yes for zip")
                            zip_for_canada = office_info.find_element_by_id("CityStateZip").text
                            zip_for_canada_final = state_for_canada.split(" ")
                            zip = str(zip_for_canada_final[-2::]).replace("[", "").replace("]", "").replace("'",                                                      "").replace(
                                ",", "")
                        else:
                            zip0 = adress_split[-1]
                            zip = " ".join(re.findall("[0-9()]+", zip0)).strip().replace(" ", "-")
                        if len(zip) >= 1:
                            zip_final = zip
                        else:
                            zip_final = not_available
                        phonenumber0 = office_info.find_element_by_id("PhoneNumber").text
                        if len(phonenumber0) >= 4:
                            office_phone = str(phonenumber0).replace("Ph: ", "")
                        else:
                            office_phone = not_available
                        email_address = office_info.find_element_by_id("innerOfficeInfo").find_element_by_tag_name("a").text
                        email = str(email_address).replace("info@covd.org", not_available)
                        lat_long0 = office_info.find_element_by_class_name("mapIt").get_attribute("onclick")
                        lat_long1 = str(lat_long0)[12:35]
                        lat_long = lat_long1.replace(")", "").replace(";", "")
                        company_name = not_available
                        job_el = driver.find_element_by_id("doctorInfo").find_elements_by_tag_name("div")
                        job_title0 = job_el[2].text
                        job_title = str(job_title0).replace("Type: ", "").strip()
                        website_el = office_info.find_element_by_id("WebSite").text
                        if len(email)>=1:
                            email = email_address
                        else:
                            email = not_available
                        if len(website_el) >= 4:
                            website = str(website_el)
                        else:
                            website = not_available
                        salutation = not_available
                        url = j
                        if len(company_name_el.text) >= 1:
                            company_name = company_name_el.text
                        else:
                            pass
                        data = [company_name, salutation, first_name, last_name, degree_desigination, job_title,
                                email,
                                website,
                                office_phone, no_of_location, city, state, zip_final, county, final_address, url,
                                no_of_location_in_this_state]
                        csv_writer.writerow(data)
                        xy = xy + 1
                        print(data)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            state_index_count = state_index_count + 1
        county_index_count = county_index_count + 1










