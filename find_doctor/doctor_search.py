from datetime import datetime,date,time
import json,codecs,requests,re
import importlib
import os.path,io,json,sys
from bs4 import BeautifulSoup
import csv
# import csv_mod
vision_rehab = ""
sports_vision=""
infant=""
url="https://www.aoa.org/doctor-locator-search/dr-locator-search-results?city=&zipcode=&miles=5&state=AL&drfirstname=&drlastname=&practicename=&gender=&iframe=false&cityInfer=&stateInfer="
req=requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
url=["https://www.aoa.org/doctor-locator-search/dr-locator-search-results?city=&zipcode=&cityInfer=&stateInfer=&miles=5&infantsee=&drfirstname=&drlastname=&practicename=&gender=&clcs=&vrs=&svs=&iframe=false&infantSeeOnly=false&state=AL&page=","https://www.aoa.org/doctor-locator-search/dr-locator-search-results?city=&zipcode=&cityInfer=&stateInfer=&miles=5&infantsee=&drfirstname=&drlastname=&practicename=&gender=&clcs=&vrs=&svs=&iframe=false&infantSeeOnly=false&state=AK&page=","https://www.aoa.org/doctor-locator-search/dr-locator-search-results?city=&zipcode=&cityInfer=&stateInfer=&miles=5&infantsee=&drfirstname=&drlastname=&practicename=&gender=&clcs=&vrs=&svs=&iframe=false&infantSeeOnly=false&state=FL&page="]
filename='new_file.csv'
fields=['Company Name','Salutation','First Name','Last Name','Vision Rehab','Sports Vision','Infant','Degree Designation','Job Title','Email Address','Website','Office Phone','Number of Locations','City','State','County(Zip)','Address','County','URL(For Verification)']
output_csv = csv.writer(open(filename,'a'))
output_csv.writerow(fields)
# with open('new_file.csv', "w") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     csv_writer.writerow(['Company Name','Salutation','First Name','Last Name','Degree Designation','Job Title','Email Address','Website','Office Phone','Number of Locations','City','State','Zip','County'])

for i in url:
    # print(i)
    for j in range(17):
        page_url=i+str(j)
        # print(page_url)

        page_url_req=requests.get(page_url)
        page_soup = BeautifulSoup(page_url_req.text, 'html.parser')
        main_class=page_soup.find("div",{"id":"main"}).find_all("div",{"class":"sub-info"})
        for subinfo in main_class:
            profile_link="https://www.aoa.org/"+subinfo.find_all("a")[-1].get("href")
            profile_link_req=requests.get(profile_link)
            profile_soup=BeautifulSoup(profile_link_req.text, 'html.parser')
            docinfo=profile_soup.find("div",{"class":"deck row-fluid widget-area"})

            try:
                loc_index=docinfo.find("div",{"class":"LocationInfo"})
                # for loc_index in location_info:
                doctors_name=docinfo.find("div",{"class":"DoctorInfoHeader"}).find("h1").text
                print(doctors_name)

                Salutation=doctors_name.split()[0]
                first_name=doctors_name.split()[1]
                last_name_index=doctors_name.split()[2:]
                last_name= " ".join(last_name_index)
                location_info=docinfo.find_all("div",{"class":"LocationInfo"})
                Number_of_Locations=len(location_info)
                Education=docinfo.find("div",{"class":"Education"}).find("p").text.strip()
                if len(Education)>4:
                    Company=Education
                else:
                    Company="N/A"
                full_address=loc_index.find("p").text.replace("(Get Directions)","").strip()
                address_split=full_address.split(",")
                Address=address_split[0].strip()
                city =address_split[-2].strip()
                state=address_split[-1].split()[0].strip()
                zip_code=address_split[-1].split()[-1].strip()
                try:
                    mobile_info=loc_index.find_all("p")[-1].text.split()
                    Mobile_text=mobile_info[0].strip()
                    if len(Mobile_text)>11:
                        Mobile_num=Mobile_text
                    else:
                        Mobile_num = "N/A "
                    print(mobile_no)

                except:
                    pass
                try:
                    website=loc_index.find_all("p")[-1].find("a").get("href")
                    # print(website)
                except:
                    website="N/A"

                try:
                    Direction_link=loc_index.find_all("p")[0].find("a").get("href")

                except:
                    Direction_link="N/A"

                try:
                    affiliation=docinfo.find("div",{"class":"DoctorAffiliation"}).find("p").text
                    print(affiliation)
                    try:
                        if(re.match(r'(?i)InfantSEE®|InfantSEE',affiliation)):
                            infant="yes"
                            print(infant)
                        else:
                            infant="N/A"
                            print(infant)
                        

                    except:
                        pass
                        
                    try:
                        if(re.match(r'(?i)Vision Rehabilitation Emphasis|Vision Rehab',affiliation)):
                            vision_rehab="yes"
                            print(vision_rehab)
                        else:
                            vision_rehab="N/A"
                            print(vision_rehab)


                        
                    except:
                        pass

                    try:
                    
                        if(re.match(r'(?i)Sports Vision|Sports Vision Emphasis',affiliation)):
                            sports_vision="yes"
                            print(sports_vision)
                        else:
                            sports_vision="N/A"
                            print(sports_vision)
                            
                    except:
                        pass
                    
                except:
                    pass

            

                CompanyName=Company
                Salutation=Salutation
                FirstName=first_name
                Last_Name=last_name
                Vision_Rehab=vision_rehab
                Sports_Vision=sports_vision
                Infant=infant
                degreeDesignation="N/A"
                JobTitle="N/A"
                EmailAddress="N/A"
                Website=website
                OfficePhone=Mobile_num
                NumberofLocations=Number_of_Locations
                City=city
                State=state
                Zip = zip_code
                Address = Address
                County = "US"
                profile_url=profile_link



                output_csv = csv.writer(open('new_file.csv','a'))
                data=[CompanyName,Salutation,FirstName,Last_Name,Vision_Rehab,Sports_Vision,Infant,degreeDesignation,JobTitle,EmailAddress,Website,OfficePhone,NumberofLocations,City,state,Zip,County,Address,profile_url]
                
                output_csv.writerow(data)
                
                print(data)
            




            except:
                print("fail")
                pass

        

       

    
    