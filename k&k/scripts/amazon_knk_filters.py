from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import numpy as np
from skimage.metrics import structural_similarity
import cv2
import pandas as pd
from PIL import Image , ImageChops
import time
import os
from selenium import webdriver
import platform
from xlrd import open_workbook
import csv

base_url = "https://www.amazon.com/gp/product/"

import shutil
import requests
from PIL import ImageFile
import xlwt
from xlwt import Workbook
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("/Users/aashishsaini/PycharmProjects/bvr_automation_suit/drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver_win.exe")
elif  platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver_linux")
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=chromepath, chrome_options = chrome_options)
chrome_options.add_argument("window-size=1920x1080")
def get_product_description():
    book = open_workbook("/Users/aashishsaini/PycharmProjects/bvr_automation_suit/data/knk.xlsx")
    sheet = book.sheet_by_index(0)
    my_list = []
    for row in range(509, 961):  # start from 1, to leave out row 0
        my_list.append(str(sheet.cell(row, 1)).replace("text:", "").replace("'", ""))  # extract from first col

    with open('../data/knk_output.csv', "w",encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ["ASIN", "Bullet 1", "Bullet 2", "Bullet 3", "Bullet 4", "Bullet 5", "Bullet 6", "Bullet 7", "Bullet 8",
             "Bullet 9", "Product Description Full"])
        driver.maximize_window()
        a=454
        for i in my_list:
            driver.get(base_url + i)
            asin_no = i
            if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." in driver.page_source:
                not_avail  = "Product Removed"
                data = [asin_no, not_avail, not_avail, not_avail, not_avail, not_avail, not_avail, not_avail, not_avail, not_avail , not_avail]
                csv_writer.writerow(data)
            else:
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
                            EC.presence_of_element_located((By.ID, "productDescription")))
                        product_description = driver.find_element_by_id("productDescription").find_element_by_tag_name("p").text
                except:
                        print("Description Not Available")
                        pass

            # "-----------------------------------------------------------------------------------------------------"
                while "Type the characters you see in this image:" in driver.page_source:
                    print("Bot got captured by amazon")
                    print("Trying to Bypass... ")
                    driver.refresh()
                try:
                    driver.find_element_by_xpath("//input[@data-action-type = 'DISMISS']").click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath("//span[@class = 'a-expander-prompt']").click()
                except:
                    try:
                        time.sleep(0.5)
                        driver.find_element_by_xpath("//span[@class = 'a-expander-prompt']").click()
                    except:
                        try:
                            driver.refresh()
                            time.sleep(0.5)
                            driver.find_element_by_xpath("//span[@class = 'a-expander-prompt']").click()
                        except:
                            pass
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "feature-bullets")))
                bullet_features = driver.find_element_by_id("feature-bullets").find_elements_by_tag_name("li")
                bullet_list = []
                for i in bullet_features:
                    if i.text == "":
                        pass
                    else:
                        bullet_list.append(i.text)

                b1 = bullet_list[0]
                b2 = bullet_list[1]
                b3 = bullet_list[2]
                b4 = bullet_list[3]
                b5 = bullet_list[4]
                b6 = bullet_list[5]
                b7 = bullet_list[6]
                b8 = bullet_list[7]
                b9 = bullet_list[8]
                data = [asin_no, b1,b2,b3,b4,b5,b6,b7,b8,b9,product_description]
                csv_writer.writerow(data)
                a= a-1
                print(a)
                print(asin_no)
def image_compare():

    book = open_workbook("/Users/aashishsaini/PycharmProjects/k&k/data/10-FEB.xlsx")
    sheet = book.sheet_by_index(0)
    my_list = []
    for row in range(1, 15):  # start from 1, to leave out row 0
        my_list.append(str(sheet.cell(row, 0)).replace("text:", "").replace("'", ""))  # extract from first col
    driver.maximize_window()

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    # with open('../data/knk_image_compare.csv', "w") as csv_file:
    #     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     csv_writer.writerow(
    #         ["ASIN", "Source image", "Target Image", "Image_Difference", "SSIM Score"])
    style = xlwt.easyxf('font: bold 1')
    sheet1.write(0,0,"ASIN",style)
    sheet1.write(0,1,"Source image",style)
    sheet1.write(0,2,"Target Image",style)
    sheet1.write(0,3,"Image_Difference",style)
    sheet1.write(0,4,"SSIM Score",style)
    sheet1.write(0,5,"MSE Score",style)

    rows=1
    column=0

    for i in my_list:
        driver.get(base_url + i)
        time.sleep(2)

        if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." in driver.page_source:
            print("product removed "+i)
        else:
            time.sleep(0.5)
            img_url = driver.find_element_by_id("imgTagWrapperId").find_element_by_tag_name("img").get_attribute("src")
            driver.get(img_url)
            driver.get(img_url)
            res = requests.get(img_url,stream=True)
            # Open a local file with wb ( write binary ) permission.
            local_file = open("/Users/aashishsaini/PycharmProjects/k&k/target_img/"+i+'.jpg', 'wb')
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            res.raw.decode_content = True
            # Copy the response stream raw data to local image file.
            shutil.copyfileobj(res.raw, local_file)
            # Remove the image url response object.
            df = pd.read_excel("/Users/aashishsaini/PycharmProjects/k&k/data/10-FEB.xlsx")
            df_abc = df[df["ASIN"] == i]  # this will only contain 2,4,6 rows
            global source_img
            for row in df_abc.itertuples():
                source_img = row[2]
            try:
                source = Image.open("../data/K&N_ROTO/Main_Images/Standard_ROTO_Resized/"+source_img+" (1).jpg")
            except:
                source = Image.open("../data/K&N_ROTO/Main_Images/Standard_ROTO_Resized/"+source_img+".jpg")

            target = Image.open("/Users/aashishsaini/PycharmProjects/k&k/target_img/"+i+".jpg")
            ImageFile.LOAD_TRUNCATED_IMAGES = True

            high_res_size = source.size
            low_res_size = target.size

            max_size = (min(high_res_size[0], low_res_size[0]), min(high_res_size[1], low_res_size[1]))

            resized_high_res_image = source.resize(max_size)
            resized_low_res_image = target.resize(max_size)

            # Image._show(resized_low_res_image)
            # Image._show(resized_high_res_image)

            resized_high_res_image.save("/Users/aashishsaini/PycharmProjects/k&k/resized_img/"+i+"_high.jpg")
            resized_low_res_image.save("/Users/aashishsaini/PycharmProjects/k&k/resized_img/"+i+"_low.jpg")
            gray_high_res = cv2.cvtColor(np.float32(resized_high_res_image), cv2.COLOR_BGR2GRAY)
            gray_low_res = cv2.cvtColor(np.float32(resized_low_res_image), cv2.COLOR_BGR2GRAY)

            (score, diff) = (structural_similarity(gray_high_res, gray_low_res, full=True))

            score = float(score)
            score = format(score,'.2f')
            mse_score = np.sum((gray_high_res.astype("float")-gray_low_res.astype("float"))**2)
            mse_score /= float(gray_high_res.shape[0]*gray_low_res.shape[1])
            mse_score = format(mse_score,'.2f')

            # thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            # contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # contours = contours[0] if len(contours) == 2 else contours[1]
            #
            # contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
            #
            # # The largest contour should be the new detected difference
            # if len(contour_sizes) > 0:
            #     largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
            #     (x, y, w, h) = cv2.boundingRect(largest_contour)
            #     cv2.rectangle(resized_high_res_image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            #     cv2.rectangle(resized_low_res_image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            # print(score)
            # cv2.imshow('diff',diff)
            # cv2.waitKey(0)
            img1 = Image.open("/Users/aashishsaini/PycharmProjects/k&k/resized_img/"+i+"_high.jpg")
            img2 = Image.open("/Users/aashishsaini/PycharmProjects/k&k/resized_img/"+i+"_low.jpg")
            diff1 = ImageChops.difference(img1, img2)
            global diff_img
            if diff1.getbbox():
                diff1.save("/Users/aashishsaini/PycharmProjects/k&k/difference/"+i+"_diff.jpg")

            amazon_img = ("file:///Users/aashishsaini/PycharmProjects/k&k/target_img/"+i+".jpg")
            local_img = ("file:///Users/aashishsaini/PycharmProjects/k&k/data/K&N_ROTO/Main_Images/Standard_ROTO_Resized/"+source_img+" (1).jpg")
            diff_img = ("file:///Users/aashishsaini/PycharmProjects/k&k/difference/"+i+"_diff.jpg")
            data = (i,local_img,amazon_img,diff_img,score)
            print(data)
            high_style = xlwt.easyxf('font: bold 1, color red;')
            # cell_style = xlwt.ea
            # csv_writer.writerow(data)
            sheet1.write(rows,column,str(i))
            sheet1.write(rows,column+1,str(local_img))
            sheet1.write(rows,column+2,str(amazon_img))
            sheet1.write(rows,column+3,str(diff_img))
            if score < str(0.85):
                sheet1.write(rows,column+4,str(score),high_style)
            else:
                sheet1.write(rows,column+4,str(score),)
            sheet1.write(rows,column+5,str(mse_score))
            wb.save("knk_image_compare.xls")
            rows = rows+1

image_compare()

