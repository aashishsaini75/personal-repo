from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os
from selenium import webdriver
import platform

asin_no = input(("Please enter the asin no. "))
filename = asin_no + ".json"
data = {}
time_list = [0,0]
data['features'] = []
data['reviewsAspects'] = []
data['productInformation'] = []
data['features'] = []
data['productDescription'] = []
data['reviews'] = []
data['qAndA'] = []
base_url = "https://www.amazon.com/gp/product/"
ques_base_url = "https://www.amazon.com/ask/questions/asin/"
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver_linux")
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromepath, chrome_options = chrome_options)
chrome_options.add_argument("window-size=1920x1080")
def get_product_detail():
    print("getting product detail...")
    driver.get(str(base_url + asin_no).strip())
    driver.maximize_window()
    driver.refresh()
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        print("Trying to Bypass... ")
        driver.refresh()
    product_title = ""
    manufacturer_name = ""
    current_price = ""
    rating = ""
    total_ratings = ""
    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass
    try:
        product_title = driver.find_element_by_id("productTitle").text
        print(product_title)
        manufacturer_name = driver.find_element_by_id("bylineInfo").text
    except:
        try:
            product_title = driver.find_element_by_id("ebooksProductTitle").text
            print(product_title)
        except:
            pass
    try:
        current_price = driver.find_element_by_id("priceblock_saleprice").text
    except:
        try:
            current_price = driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass
    try:
        rating = driver.find_element_by_id("acrPopover").get_attribute("title")
        total_ratings = driver.find_element_by_xpath("//span[@id = 'acrCustomerReviewText']").text
    except:
        pass

    product_detail = {
        "productURL":base_url+asin_no,
                      "ASIN": asin_no,
                        "title": product_title,
                      "manufacturer": manufacturer_name,
                      "currentPrice": current_price,
                      "rating": str(rating).replace(" out of 5 stars",""),
                      "totalRatings": str(total_ratings).replace("ratings","")
                      }
    data.update(product_detail)
def get_review_Aspects():
    print("getting review aspects...")
    driver.get(base_url + asin_no + "#customerReviews")
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        driver.refresh()
        print("Trying to Bypass... ")
    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "acrCustomerReviewText")))
        driver.find_element_by_id("acrCustomerReviewText").click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"cr-lighthouse-terms")))
        review_aspects_el = driver.find_element_by_class_name("cr-lighthouse-terms").find_elements_by_class_name(
            "cr-lighthouse-term ")
        for i in review_aspects_el:
            if i.text == "":
                pass
            else:
                data['reviewsAspects'].append(i.text)
    except:
        try:
            driver.get(base_url + asin_no + "#customerReviews")
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"cr-lighthouse-terms")))

            review_aspects_el = driver.find_element_by_class_name("cr-lighthouse-terms").find_elements_by_class_name(
                "cr-lighthouse-term ")
            for i in review_aspects_el:
                if i.text == "":
                    pass
                else:
                    data['reviewsAspects'].append(i.text)
        except:
            pass

def get_product_information():
    product_spec = ""
    print("getting product information...")
    driver.get(base_url + asin_no)
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        driver.refresh()
        print("Trying to Bypass... ")
    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass
    try:
        product_spec = driver.find_element_by_id("productDetails_detailBullets_sections1").find_elements_by_tag_name("tr")
    except:
        pass
    dict = {}
    for i in product_spec:
        key = i.find_elements_by_tag_name("th")[0].text
        value = i.find_elements_by_tag_name("td")[0].text
        dict[key] = value
    data['productInformation'].append(dict)

def get_product_description():
    print("getting product description...")
    driver.get(base_url + asin_no)
    driver.maximize_window()
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        driver.refresh()
        print("Trying to Bypass... ")
    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "aplus")))
        product_description = driver.find_element_by_id("aplus").text
        data['productDescription'] = str(product_description).replace("Product Description","").replace("Product description","")
    except:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "productDescription_feature_div")))
            product_description = driver.find_element_by_id("productDescription_feature_div").text
            data['productDescription'] = str(product_description).replace("Product Description","")
        except:
            print("Description Not Available")
            pass
def get_product_features():
    print("getting product features...")
    driver.get(base_url + asin_no)
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        print("Trying to Bypass... ")
        driver.refresh()
    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "feature-bullets")))
        bullet_features = driver.find_element_by_id("feature-bullets").find_elements_by_tag_name("li")
        for i in bullet_features:
            if i.text == "":
                pass
            else:
                data['features'].append(i.text)
    except:
        print(Exception)
        pass

def get_product_QA():

    print("getting product Q&A...")
    driver.get(ques_base_url+asin_no)
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        print("Trying to Bypass... ")
        driver.refresh()
    try:
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@class = 'a-section askTeaserQuestions']")))
    except:
        return
    if "a-disabled a-last" not in driver.page_source:
        while "a-disabled a-last" not in driver.page_source:
            main_block = driver.find_element_by_xpath("//*[@class = 'a-section askTeaserQuestions']")
            blocks = main_block.find_elements_by_xpath("//*[@class='a-fixed-left-grid a-spacing-base']")[::2]
            for i in blocks:
                question = i.find_elements_by_tag_name("span")[6]
                answer = "Answer not available"
                try:
                    answer_text = i.find_elements_by_tag_name("span")[8].text
                    if "Answer:" in answer_text:
                        answer = i.find_elements_by_tag_name("span")[9].text
                    else:
                        answer = i.find_elements_by_tag_name("span")[8].text
                except:
                    pass
                q_and_a = {"question": question.text,
                           "answer": answer
                           }
                data['qAndA'].append(q_and_a)

            driver.find_element_by_xpath("//*[@class ='a-last']").click()

        if "a-disabled a-last" in driver.page_source:
            main_block = driver.find_element_by_xpath("//*[@class = 'a-section askTeaserQuestions']")
            blocks = main_block.find_elements_by_xpath("//*[@class='a-fixed-left-grid a-spacing-base']")[::2]
            for j in blocks:
                question = j.find_elements_by_tag_name("span")[6]
                answer = "Answer not available"
                try:
                    answer_text = j.find_elements_by_tag_name("span")[8].text
                    if "Answer:" in answer_text:
                        answer = j.find_elements_by_tag_name("span")[9].text
                    else:
                        answer = j.find_elements_by_tag_name("span")[8].text
                except:
                    pass
                q_and_a = {"question": question.text,
                           "answer": answer
                           }
                data['qAndA'].append(q_and_a)

def get_product_reviews():
    chromepath = ""
    if platform.system() == "Darwin":
        chromepath = os.path.abspath("drivers/chromedriver")
    elif platform.system() == "Windows":
        chromepath = os.path.abspath("drivers/chromedriver_win.exe")
    elif platform.system() == 'Linux':
        chromepath = os.path.abspath("drivers/chromedriver_linux")
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromepath , chrome_options=chrome_options)
    chrome_options.add_argument("window-size=1920x1080")
    print("getting product reviews...")
    driver.get(base_url+asin_no+"#customerReviews")
    driver.get(base_url+asin_no+"#customerReviews")
    driver.maximize_window()
    while "Type the characters you see in this image:" in driver.page_source:
        print("Bot got captured by amazon")
        print("Trying to Bypass... ")
        driver.refresh()
    try:
        driver.find_element_by_xpath("//a[@data-hook= 'see-all-reviews-link-foot']").click()
    except:
        pass

    try:
        driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
    except:
        pass
    time.sleep(5)
    if "a-disabled a-last" not in driver.page_source:
        while "a-disabled a-last" not in driver.page_source:
            if "Sorry, no reviews match your current selections." in driver.page_source:
                print("Sorry, no reviews match your current selections")
                return
            elif "No customer reviews" in driver.page_source:
                return
            else:
                cleaned_response = driver.page_source
                parser = html.fromstring(cleaned_response)
                review_blocks = parser.xpath("//div[@data-hook='review']")
                for i in review_blocks:
                    reviewer_name = str(i.xpath(".//span[contains(@class,'profile-name')]//text()")).strip().replace("[","").replace("]","").replace("'","")
                    ratings =str(i.xpath(".//i[@data-hook='review-star-rating']//text()")).strip().replace("[","").replace("]","").replace("'","")
                    review_title = str(i.xpath(".//a[@data-hook='review-title']//span//text()")).strip().replace("[","").replace("]","").replace("'","")
                    review_date = str(i.xpath(".//span[@data-hook='review-date']//text()")).strip().replace("[","").replace("]","").replace("'","")
                    review_text = str(i.xpath(".//span[@data-hook='review-body']//span//text()")).strip().replace("[","").replace("]","").replace("'","")
                    product_reviews = {"reviewerName": reviewer_name,
                                   "rating": ratings,
                                   "reviewTitle": review_title,
                                   "reviewDate": review_date,
                                   "reviewText": review_text
                                   }
                    data['reviews'].append(product_reviews)

                try:
                    driver.find_element_by_xpath("//li[@class = 'a-last']").click()
                except:
                        try:
                            driver.execute_script("scroll(0, -250);")
                            time.sleep(0.5)
                            next = driver.find_element_by_xpath("//li[@class = 'a-last']")
                            driver.execute_script("arguments[0].click()", next)
                        except:
                            try:
                                time.sleep(1)
                                next = driver.find_element_by_xpath("//li[@class = 'a-last']")
                                driver.execute_script("arguments[0].click()", next)
                            except:
                                try:
                                    time.sleep(1.5)
                                    next = driver.find_element_by_xpath("//li[@class = 'a-last']")
                                    driver.execute_script("arguments[0].click()", next)
                                except:
                                    try:
                                        time.sleep(2)
                                        next = driver.find_element_by_xpath("//li[@class = 'a-last']")
                                        driver.execute_script("arguments[0].click()", next)
                                    except:
                                            try:
                                                time.sleep(3)
                                                next = driver.find_element_by_xpath("//li[@class = 'a-last']")
                                                driver.execute_script("arguments[0].click()", next)
                                            except:
                                                    cleaned_response = driver.page_source
                                                    parser = html.fromstring(cleaned_response)
                                                    review_blocks = parser.xpath("//div[@data-hook='review']")
                                                    for i in review_blocks:
                                                        reviewer_name = str(i.xpath(
                                                            ".//span[contains(@class,'profile-name')]//text()")).strip().replace(
                                                            "[",
                                                            "").replace(
                                                            "]", "").replace("'", "")
                                                        ratings = str(i.xpath(
                                                            ".//i[@data-hook='review-star-rating']//text()")).strip().replace(
                                                            "[", "").replace(
                                                            "]", "").replace("'", "")
                                                        review_title = str(i.xpath(
                                                            ".//a[@data-hook='review-title']//span//text()")).strip().replace(
                                                            "[",
                                                            "").replace(
                                                            "]", "").replace("'", "")
                                                        review_date = str(i.xpath(
                                                            ".//span[@data-hook='review-date']//text()")).strip().replace(
                                                            "[", "").replace(
                                                            "]", "").replace("'", "")
                                                        review_text = str(i.xpath(
                                                            ".//span[@data-hook='review-body']//span//text()")).strip().replace(
                                                            "[",
                                                            "").replace(
                                                            "]", "").replace("'", "")
                                                        product_reviews = {"reviewerName": reviewer_name,
                                                                           "rating": ratings,
                                                                           "reviewTitle": review_title,
                                                                           "reviewDate": review_date,
                                                                           "reviewText": review_text
                                                                           }
                                                        data['reviews'].append(product_reviews)
                                                        return

                driver.execute_script("scroll(0, -250);")
                time.sleep(2)
        if "a-disabled a-last"  in driver.page_source:
            cleaned_response = driver.page_source
            parser = html.fromstring(cleaned_response)
            review_blocks = parser.xpath("//div[@data-hook='review']")
            for i in review_blocks:
                reviewer_name = str(i.xpath(".//span[contains(@class,'profile-name')]//text()")).strip().replace("[",
                                                                                                                 "").replace(
                    "]", "").replace("'", "")
                ratings = str(i.xpath(".//i[@data-hook='review-star-rating']//text()")).strip().replace("[", "").replace(
                    "]", "").replace("'", "")
                review_title = str(i.xpath(".//a[@data-hook='review-title']//span//text()")).strip().replace("[",
                                                                                                             "").replace(
                    "]", "").replace("'", "")
                review_date = str(i.xpath(".//span[@data-hook='review-date']//text()")).strip().replace("[", "").replace(
                    "]", "").replace("'", "")
                review_text = str(i.xpath(".//span[@data-hook='review-body']//span//text()")).strip().replace("[",
                                                                                                              "").replace(
                    "]", "").replace("'", "")
                product_reviews = {"reviewerName": reviewer_name,
                                   "rating": ratings,
                                   "reviewTitle": review_title,
                                   "reviewDate": review_date,
                                   "reviewText": review_text
                                   }
                data['reviews'].append(product_reviews)

get_product_information()
get_product_description()
get_review_Aspects()
get_product_detail()
get_product_features()
get_product_QA()
driver.quit()
get_product_reviews()
with open(filename, 'w') as json_file:
    json.dump(data, json_file)
    print("Product Scraped Successfully")
