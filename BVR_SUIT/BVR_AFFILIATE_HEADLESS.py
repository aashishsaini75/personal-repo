from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import clipboard
import time
import pickle
from selenium import webdriver
from slacker import Slacker
slack = Slacker("xoxb-375138887649-624148466112-JrgRf8XvhZrzApdAzPoEks7h")
interfaceurl = "http://bestviewsreviews.com/submit-affiliate-link/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')
chrome_options.add_argument(f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')
driver = webdriver.Chrome(executable_path='/Users/aashishsaini/PycharmProjects/BVR_SUIT/web_drivers/chromedriver',chrome_options = chrome_options)
driver.get(interfaceurl)
time.sleep(0.3)
# driver.execute_script("window.open('https://affiliate-program.amazon.com/');")
driver.execute_script("window.open('https://affiliate-program.amazon.com/');")
time.sleep(0.3)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
driver.find_element_by_class_name("a-button-text").click()
time.sleep(0.3)
# driver.find_element_by_name("email").send_keys("info@parkcircletech.com")
driver.find_element_by_name("email").send_keys("ranjeeta@parkcircletech.com")
# driver.find_element_by_name("password").send_keys("Parkcircle123")
driver.find_element_by_name("password").send_keys("ranjeeta123")
driver.find_element_by_id("signInSubmit").click()
time.sleep(0.3)
slack.chat.post_message("#Automation_report_bot",
                        "Machine 1=  Automation Suit Started")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.quit()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument('--user-data-dir =/private/var/folders/90/9kfx9cfn0979236jmjn1py0r0000gn/T/.org.chromium.Chromium.YVtCko/Default')
chrome_options.add_argument(f'user-agent={"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}')

driver = webdriver.Chrome(executable_path='/Users/aashishsaini/PycharmProjects/BVR_SUIT/web_drivers/chromedriver',chrome_options = chrome_options)
cookies = pickle.load(open("cookies.pkl", "rb"))
driver.maximize_window()
driver.get(interfaceurl)
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(0.3)
# driver.execute_script("window.open('https://affiliate-program.amazon.com/');")
driver.execute_script("window.open('https://affiliate-program.amazon.com/');")
time.sleep(10)
j=0
a=0
b=0
while a==0:
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.3)
    while len(driver.find_element_by_id("asin_text").get_attribute("value"))!= 10:
        print(driver.find_element_by_id("asin_text").get_attribute("value"))
        driver.refresh()
        time.sleep(0.5)
    asin_val  = driver.find_element_by_id("asin_text").get_attribute("value")
    time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[-1])
    # driver.save_screenshot("loopstart.png")
    time.sleep(0.3)
    driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
    time.sleep(0.3)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(2)
    while "No results found" in driver.page_source:
        # output_csv2.writerow([asin_val])
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_id("product_clipboard").click()
        driver.find_element_by_id("product_clipboard").click()
        time.sleep(0.5)
        driver.find_element_by_name("buy_url").send_keys(clipboard.paste())
        driver.find_element_by_name("image_snippet").send_keys('<img src = "https://s3-us-west-2.amazonaws.com/data.bestviewsreviews.com/CATEGORY_IMG/no-image.jpg">' )
        submit = driver.find_element_by_name("submit")
        driver.execute_script("arguments[0].click();", submit)
        b=b+1
        print("No of Affiliate Link updated updated with product url = " + str(b)+"Asin No Is - "+asin_val)
        while len(driver.find_element_by_id("asin_text").get_attribute("value")) != 10:
            print(driver.find_element_by_id("asin_text").get_attribute("value"))
            # output_csv.writerow([driver.find_element_by_id("asin_text").get_attribute("value")])
            driver.refresh()
            time.sleep(0.5)
        asin_val = driver.find_element_by_id("asin_text").get_attribute("value")
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_xpath("//*[@placeholder='keyword or ASIN/ISBN']").clear()
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[@type ='search']").clear()
        driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(2)
    try:

        WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
        c= driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
        c[1].click()

    except:

        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get("https://affiliate-program.amazon.com/")
            driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
            driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(0.3)
            WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
            c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
            c[1].click()
        except:
            try:
                for cookie in cookies:
                    driver.add_cookie(cookie)
                driver.get("https://affiliate-program.amazon.com/")
                driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
                driver.find_element_by_xpath("//*[@type='submit']").click()
                time.sleep(0.5)
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//*[@title='Build links and widgets for this product']")))
                c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
                c[1].click()
            except:

                slack.chat.post_message("#automation_report_bot", "MACHINE 2(Atul): Automation Suit broke, Please restart the Suit!")
    try:
        time.sleep(0.3)
        driver.get_screenshot_as_file("TextOnly.png")
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@title ='Text Only']")))
        driver.find_element_by_xpath("//*[@title ='Text Only']").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")))
        link = driver.find_element_by_xpath("//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")
        driver.execute_script("arguments[0].click();", link)
    except:
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://affiliate-program.amazon.com/")
        # driver.save_screenshot("link.png")
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@type ='search']")))
        driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
        c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
        c[1].click()
        time.sleep(1.5)
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@title ='Text Only']")))
            driver.find_element_by_xpath("//*[@title ='Text Only']").click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")))
            link = driver.find_element_by_xpath("//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")
            driver.execute_script("arguments[0].click();", link)
        except:
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get("https://affiliate-program.amazon.com/")
            # driver.save_screenshot("link.png")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@type ='search']")))
            driver.find_element_by_xpath("//*[@type ='search']").send_keys(asin_val)
            driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@title='Build links and widgets for this product']")))
            c = driver.find_elements_by_xpath("//*[@title='Build links and widgets for this product']")
            c[1].click()
            time.sleep(2)
            # driver.save_screenshot("tEXT_ONLY EXPECT..png")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@title ='Text Only']")))
            driver.find_element_by_xpath("//*[@title ='Text Only']").click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")))
            link = driver.find_element_by_xpath("//*[@class ='a-label a-radio-label' and contains(text(),'Short Link')]")
            driver.execute_script("arguments[0].click();", link)
    try:
        time.sleep(0.3)
        for i in range(5):
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']")))
            driver.find_element_by_xpath("//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']").click()
    except:
        driver.refresh()
        time.sleep(1)
        for i in range(5):
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']")))
            driver.find_element_by_xpath("//*[@class ='ac-ad-code-area ac-hidden ac-ad-code-short']").click()
            time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.3)
    buy_url = driver.find_element_by_name("buy_url")
    driver.execute_script("arguments[0].click();",buy_url)
    time.sleep(0.3)
    driver.find_element_by_name("buy_url").send_keys(clipboard.paste())
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(0.3)
    driver.find_element_by_xpath("//a[@title='Image Only']").click()
    time.sleep(0.3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.2)
    driver.execute_script("arguments[0].click();",
                                                    driver.find_element_by_id("ac-productlinks-ad-code-panel-image-button-announce"))
    time.sleep(0.3)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://affiliate-program.amazon.com/")
    # driver.find_element_by_xpath("//*[@title='Home']").click()
    while "Amazon.in Associates Central - Customize and Get HTML" == driver.title:
        driver.refresh()
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://affiliate-program.amazon.com/")

    while "Amazon.in Associates: The web's most popular and successful Affiliate Program" == driver.title:
        # driver.save_screenshot("home_click.png")
        driver.refresh()
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.find_element_by_class_name("a-button-text").click()
        time.sleep(0.3)
        # driver.find_element_by_name("email").send_keys("info@parkcircletech.com")
        driver.find_element_by_name("email").send_keys("ranjeeta@parkcircletech.com")
        # driver.find_element_by_name("password").send_keys("Parkcircle123")
        driver.find_element_by_name("password").send_keys("ranjeeta123")
        driver.find_element_by_id("signInSubmit").click()
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.3)
    driver.find_element_by_name("image_snippet").send_keys(clipboard.paste())
    submit = driver.find_element_by_name("submit")
    driver.execute_script("arguments[0].click();",submit)
    j=j+1
    print("No of Affiliate Link updated = "+str(j))
    # driver.save_screenshot("loop_end.png")
