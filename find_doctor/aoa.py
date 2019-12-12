from selenium import webdriver
import requests, re
from bs4 import BeautifulSoup
import csv
import time
import socket

def aoa_scrap():
        filename = 'new_file.csv'
        fields = ['Company Name', 'Salutation', 'First Name', 'Last Name', 'Vision Rehab', 'Sports Vision', 'Infant',
                  'Degree Designation', 'Job Title', 'Email Address', 'Website', 'Office Phone', 'Number of Locations', 'City',
                  'State', 'County(Zip)', 'Address', 'County', 'URL(For Verification)']
        output_csv = csv.writer(open(filename, 'a', newline=''))
        output_csv.writerow(fields)
        url = "https://www.aoa.org/doctor-locator-search?tab=basic"
        driver = webdriver.Chrome(executable_path="/Users/aashishsaini/PycharmProjects/amazon-scraper/drivers/chromedriver")
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_xpath("//a[@href = '#advanced']").click()
        state_list = driver.find_element_by_id("state").find_elements_by_tag_name("option")
        state_list1 = []
        for i in state_list:
            state_list1.append(i.get_attribute("value"))
        while '' in state_list1:
            state_list1.remove('')
        url1 = "https://www.aoa.org/doctor-locator-search/dr-locator-search-results?miles=50&state="
        print(state_list1)
        a = 31
        for j in range(len(state_list1[31:])):
            url_2 = url1 + str(state_list1[a])
            driver.get(url_2)
            pagination_class = driver.find_element_by_xpath("//div[@class='pagination']").text
            while (re.search(r'(?i)Next', pagination_class)):
                time.sleep(0.5)
                pagination_class = driver.find_element_by_xpath("//div[@class='pagination']").text
                page_url_req = driver.page_source
                page_soup = BeautifulSoup(page_url_req, 'html.parser')
                main_class = page_soup.find("div", {"id": "main"}).find_all("div", {"class": "sub-info"})
                if (re.search(r'(?i)Next', pagination_class)):
                    for subinfo in main_class:
                        vision_rehab = ""
                        sports_vision = ""
                        infant = ""
                        profile_link = "https://www.aoa.org/" + subinfo.find_all("a")[-1].get("href")
                        profile_link_req = requests.get(profile_link)
                        profile_soup = BeautifulSoup(profile_link_req.text, 'html.parser')
                        docinfo = profile_soup.find("div", {"class": "deck row-fluid widget-area"})
                        loc_index = docinfo.find_all("div", {"class": "LocationInfo"})
                        for loc in loc_index:
                            doctors_name = docinfo.find("div", {"class": "DoctorInfoHeader"}).find("h1").text
                            Salutation = doctors_name.split()[0]
                            first_name = doctors_name.split()[1]
                            last_name_index = doctors_name.split()[2:]
                            last_name = " ".join(last_name_index)
                            location_info = docinfo.find_all("div", {"class": "LocationInfo"})
                            Number_of_Locations = len(location_info)
                            try:
                                Education = docinfo.find("div", {"class": "Education"}).find("p").text.strip()
                                if len(Education) > 4:
                                    Company = Education
                                else:
                                    Company = "N/A"
                            except:
                                Company = "N/A"
                            full_address = ""
                            try:
                                full_address = loc.find("p").text.replace("(Get Directions)", "").strip()

                                address_split = full_address.split(",")
                                Address = address_split[0].strip()
                                city = address_split[-2].strip()
                                state = address_split[-1].split()[0].strip()
                                zip_code = address_split[-1].split()[-1].strip()
                            except:
                                pass
                            try:
                                mobile_info = loc.find_all("p")[-1].text.split()
                                Mobile_text = mobile_info[0].strip()
                                if len(Mobile_text) > 11:
                                    Mobile_num = Mobile_text
                                else:
                                    Mobile_num = "N/A "
                            except:
                                pass

                            try:
                                website = loc.find_all("p")[-1].find("a").get("href")
                                # print(website)
                            except:
                                website = "N/A"

                            try:
                                Direction_link = loc.find_all("p")[0].find("a").get("href")

                            except:
                                Direction_link = "N/A"

                            try:
                                affiliation = docinfo.find("div", {"class": "DoctorAffiliation"}).find("p").text
                                if (re.search(r'(?i)InfantSEE®|InfantSEE', affiliation)):
                                    infant = "Yes"
                                else:
                                    infant = "No"

                                if (re.search(r'(?i)Vision Rehabilitation Emphasis|Vision Rehab', affiliation)):
                                    vision_rehab = "Yes"
                                else:
                                    vision_rehab = "No"

                                if (re.search(r'(?i)Sports Vision|Sports Vision Emphasis', affiliation)):
                                    sports_vision = "yes"
                                else:
                                    sports_vision = "No"

                                # if "InfantSEE®"or "InfantSEE" in affiliation:
                                #     infant = "Yes"
                                # else:
                                #     infant = "No"
                                #
                                # if "Vision Rehabilitation Emphasis" or "Vision Rehab"in affiliation:
                                #     vision_rehab = "Yes"
                                # else:
                                #     vision_rehab = "No"
                                #
                                #
                                # if "Sports Vision"or "Sports Vision Emphasis" in affiliation:
                                #     sports_vision = "Yes"
                                # else:
                                #     sports_vision = "No"
                            except:
                                infant = "No"
                                vision_rehab = "No"
                                sports_vision = "No"

                            CompanyName = Company
                            Salutation = Salutation
                            FirstName = first_name
                            Last_Name = last_name
                            Vision_Rehab = vision_rehab
                            Sports_Vision = sports_vision
                            Infant = infant
                            degreeDesignation = "N/A"
                            JobTitle = "N/A"
                            EmailAddress = "N/A"
                            Website = website
                            OfficePhone = Mobile_num
                            NumberofLocations = Number_of_Locations
                            City = city
                            State = state
                            Zip = zip_code
                            Address = Address
                            County = "US"
                            profile_url = profile_link

                            output_csv = csv.writer(open('new_file.csv', 'a', newline=''))
                            data = [CompanyName, Salutation, FirstName, Last_Name, Vision_Rehab, Sports_Vision, Infant,
                                    degreeDesignation, JobTitle, EmailAddress, Website, OfficePhone, NumberofLocations,
                                    City, state, Zip, County, Address, profile_url]

                            output_csv.writerow(data)
                            print(data)
                elif "Next" not in pagination_class:
                    for subinfo in main_class:
                        profile_link = "https://www.aoa.org/" + subinfo.find_all("a")[-1].get("href")
                        profile_link_req = requests.get(profile_link)
                        profile_soup = BeautifulSoup(profile_link_req.text, 'html.parser')
                        docinfo = profile_soup.find("div", {"class": "deck row-fluid widget-area"})
                        try:
                            loc_index = docinfo.find_all("div", {"class": "LocationInfo"})
                            for loc in loc_index:
                                # for loc_index in location_info:
                                doctors_name = docinfo.find("div", {"class": "DoctorInfoHeader"}).find("h1").text
                                # print(doctors_name)
                                Salutation = doctors_name.split()[0]
                                first_name = doctors_name.split()[1]
                                last_name_index = doctors_name.split()[2:]
                                last_name = " ".join(last_name_index)
                                location_info = docinfo.find_all("div", {"class": "LocationInfo"})
                                Number_of_Locations = len(location_info)
                                try:
                                    Education = docinfo.find("div", {"class": "Education"}).find("p").text.strip()
                                    if len(Education) > 4:
                                        Company = Education
                                    else:
                                        Company = "N/A"
                                except:
                                    Company = "N/A"
                                try:
                                    full_address = loc.find("p").text.replace("(Get Directions)", "").strip()

                                    address_split = full_address.split(",")
                                    Address = address_split[0].strip()
                                    city = address_split[-2].strip()
                                    state = address_split[-1].split()[0].strip()
                                    zip_code = address_split[-1].split()[-1].strip()
                                except:
                                    pass
                                try:
                                    mobile_info = loc.find_all("p")[-1].text.split()
                                    Mobile_text = mobile_info[0].strip()
                                    if len(Mobile_text) > 11:
                                        Mobile_num = Mobile_text
                                    else:
                                        Mobile_num = "N/A "
                                except:
                                    pass

                                try:
                                    website = loc.find_all("p")[-1].find("a").get("href")
                                    # print(website)
                                except:
                                    website = "N/A"

                                try:
                                    Direction_link = loc.find_all("p")[0].find("a").get("href")

                                except:
                                    Direction_link = "N/A"

                                try:
                                    affiliation = docinfo.find("div", {"class": "DoctorAffiliation"}).find("p").text
                                    if (re.search(r'(?i)InfantSEE®|InfantSEE', affiliation)):
                                        infant = "Yes"
                                    else:
                                        infant = "No"

                                    if (re.search(r'(?i)Vision Rehabilitation Emphasis|Vision Rehab', affiliation)):
                                        vision_rehab = "Yes"
                                    else:
                                        vision_rehab = "No"

                                    if (re.search(r'(?i)Sports Vision|Sports Vision Emphasis', affiliation)):
                                        sports_vision = "yes"
                                    else:
                                        sports_vision = "No"
                                except:
                                    infant = "No"
                                    vision_rehab = "No"
                                    sports_vision = "No"

                                CompanyName = Company
                                Salutation = Salutation
                                FirstName = first_name
                                Last_Name = last_name
                                Vision_Rehab = vision_rehab
                                Sports_Vision = sports_vision
                                Infant = infant
                                degreeDesignation = "N/A"
                                JobTitle = "N/A"
                                EmailAddress = "N/A"
                                Website = website
                                OfficePhone = Mobile_num
                                NumberofLocations = Number_of_Locations
                                City = city
                                State = state
                                Zip = zip_code
                                Address = Address
                                County = "US"
                                profile_url = profile_link

                                output_csv = csv.writer(open('new_file.csv', 'a', newline=''))
                                data = [CompanyName, Salutation, FirstName, Last_Name, Vision_Rehab, Sports_Vision, Infant,
                                        degreeDesignation, JobTitle, EmailAddress, Website, OfficePhone, NumberofLocations,
                                        City, state, Zip, County, Address, profile_url]

                                output_csv.writerow(data)

                                print(data)
                        except:
                            pass
                try:
                    driver.find_element_by_xpath("//a[contains (text(), 'Next')]").click()
                except:
                    pass
            a = a + 1

aoa_scrap()
