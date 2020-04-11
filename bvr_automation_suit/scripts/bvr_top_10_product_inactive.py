from selenium import webdriver
import pymsteams
import time
import csv
import requests
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/b3a5e626-8dd4-4987-9e58-7dab05972f37@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/a8546ebb7c074509b16ba5cd6ded79b8/47631de8-81c9-4b66-8cc3-1290c874fdf4")

# myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/70f03e61-7587-4e07-b4b7-7fc89e589cf5@85a77b6c-a790-4bcf-8fd6-c1f891dd360b/IncomingWebhook/6640fc79c06b42a7b09330803add3e39/21bde621-fde7-4e25-8007-bb1ded8aad73")

data1 = {"active":False}
dpl_update_url = "https://dpl.bestviewsreviews.com/api/product/"
prod_update_url = "https://bestviewsreviews.com/api/product/"
dev_update_url = "https://dev1.bestviewsreviews.com/api/product/"
dev_url = "https://dev1.bestviewsreviews.com/all/"
prod_url = "https://bestviewsreviews.com/all/"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
driver.get(prod_url)
driver.maximize_window()
links = []
cat = driver.find_element_by_xpath("//*[@class = 'four-division all_categories_footer']").find_elements_by_xpath("//ul[@style ='display: flex;']")
for i in cat:
    var = i.find_element_by_tag_name("a").get_attribute("href")
    links.append(var)
with open('../data/BVR_Product_disable.csv', "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["ASIN","Product URL" ,"Reason"])
    for j in links:
        print(str(j).split("/")[-2])
        try:
            driver.get(j)
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to find again')
            pass
        top_prod = driver.find_elements_by_class_name("top-products")
        for k in top_prod:
            cat_name_el = k.find_element_by_xpath("//ul[@class = 'breadcrumb']").find_elements_by_tag_name("li")
            cat_name = cat_name_el[1].text
            product_url = k.find_element_by_class_name("name").find_element_by_tag_name("a").get_attribute("href")
            title = k.find_element_by_class_name("name").text
            try:
                k.find_element_by_class_name("main-product-name").click()
            except:
                time.sleep(0.3)
                driver.find_element_by_xpath("//span[@class = 'close']").click()
                k.find_element_by_class_name("main-product-name").click()
                time.sleep(0.5)
            driver.switch_to.window(driver.window_handles[1])
            asin_code = str(driver.current_url).split("/")[-2]
            if "The requested resource was not found on this server." in driver.page_source:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # create the section
                myMessageSection = pymsteams.cardsection()
                # Section Title
                myMessageSection.title(" 📢 NOTICE ⚠️")
                # Activity Elements
                myMessageSection.activityTitle("Affiliate data missing ")
                myMessageSection.activityText("The following category's product affiliate URL is missing ")
                # Facts are key value pairs displayed in a list.
                myMessageSection.addFact("Category: ",cat_name)
                myMessageSection.addFact("Product title", title)
                myMessageSection.addFact("Product URL", product_url)
                myMessageSection.addFact("Date & Time", dt_string)
                # Section Text
                myMessageSection.text("Product Details")
                # Section Images
                myTeamsMessage.summary("summary")
                # Add your section to the connector card object before sending
                myTeamsMessage.addSection(myMessageSection)
                myTeamsMessage.send()

            elif  "We don't know when or if this item will be back in stock." in driver.page_source:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # create the section
                myMessageSection = pymsteams.cardsection()
                # Section Title
                myMessageSection.title("📢 INFORMATION ⚠️")
                # Activity Elements
                myMessageSection.activityTitle("OUT OF STOCK")
                myMessageSection.activityText("The following category's product is out of stock at Amazon.com")
                # Facts are key value pairs displayed in a list.
                myMessageSection.addFact("Category: ", cat_name)
                myMessageSection.addFact("ASIN Code: ",asin_code)
                myMessageSection.addFact("Product title", title)
                myMessageSection.addFact("Product URL", product_url)
                myMessageSection.addFact("Date & Time", dt_string)
                # Section Text
                myMessageSection.text("Product Details")
                # Section Images
                myTeamsMessage.summary("summary")
                # Add your section to the connector card object before sending
                myTeamsMessage.addSection(myMessageSection)
                myTeamsMessage.send()
                res0 = requests.put(url=dev_update_url + asin_code +"/"+ "update", data=data1,
                                   headers={'Authorization': "Token f099e89c7ccbe3a1a742a7a93cd1a0f2c1b30b33"})
                res1 = requests.put(url=dpl_update_url + asin_code +"/"+ "update", data=data1,
                                   headers={'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"})
                res2 = requests.put(url=prod_update_url + asin_code +"/"+ "update", data=data1,
                                   headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
                print(str(asin_code)+" Product Updated Successfully ")
                # data = [asin_code,product_url,"OUT OF STOCK"]
                # csv_writer.writerow(data)

            elif "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." in driver.page_source:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # create the section
                myMessageSection = pymsteams.cardsection()
                # Section Title
                myMessageSection.title(" ⚠️ WARNING ⚠️")
                # Activity Elements
                myMessageSection.activityTitle("Product is Removed")
                myMessageSection.activityText("The following category's product has been removed from Amazon.com")
                # Facts are key value pairs displayed in a list.
                myMessageSection.addFact("Category: ", cat_name)
                myMessageSection.addFact("ASIN Code: ",asin_code)
                myMessageSection.addFact("Product title", title)
                myMessageSection.addFact("Product URL", product_url)
                myMessageSection.addFact("Date & Time", dt_string)
                # Section Text
                myMessageSection.text("Product Details")
                # Section Images
                myTeamsMessage.summary("summary")
                # Add your section to the connector card object before sending
                myTeamsMessage.addSection(myMessageSection)
                myTeamsMessage.send()
                res0 = requests.put(url=dev_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token f099e89c7ccbe3a1a742a7a93cd1a0f2c1b30b33"})
                res1 = requests.put(url=dpl_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"})
                res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
                print(str(asin_code)+" Product Updated Successfully ")

                # data = [asin_code, product_url, "Product is Removed"]
                # csv_writer.writerow(data)
            elif "No Product matches the given query." in driver.page_source:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # create the section
                myMessageSection = pymsteams.cardsection()
                # Section Title
                myMessageSection.title(" ⚠️ WARNING ⚠️")
                # Activity Elements
                myMessageSection.activityTitle("No Affiliate URL ")
                myMessageSection.activityText("The following category's product has been removed from Amazon.com")
                # Facts are key value pairs displayed in a list.
                myMessageSection.addFact("Category: ", cat_name)
                myMessageSection.addFact("ASIN Code: ",asin_code)
                myMessageSection.addFact("Product title", title)
                myMessageSection.addFact("Product URL", product_url)
                myMessageSection.addFact("Date & Time", dt_string)
                # Section Text
                myMessageSection.text("Product Details")
                # Section Images
                myTeamsMessage.summary("summary")
                # Add your section to the connector card object before sending
                myTeamsMessage.addSection(myMessageSection)
                myTeamsMessage.send()
                res0 = requests.put(url=dev_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token f099e89c7ccbe3a1a742a7a93cd1a0f2c1b30b33"})
                res1 = requests.put(url=dpl_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token 5abd3a487ad4023482ce0379faad475916263b88"})
                res2 = requests.put(url=prod_update_url + asin_code + "/" + "update", data=data1,
                                    headers={'Authorization': "Token 658dd0395badb9fe407ea6a16763458a14accb87"})
                print(str(asin_code)+" Product Updated Successfully ")
                # data = [asin_code, product_url, "affiliate data not available"]
                # csv_writer.writerow(data)
            else:
                pass
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
driver.quit()


