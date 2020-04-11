from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")

url = "http://ekata.shorthillstech.com/"

driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
driver.get(url)
driver.maximize_window()
driver.fullscreen_window()
driver.find_element_by_xpath("//a[@href = '/login/']").click()
driver.find_element_by_xpath("//input[@name = 'username']").send_keys("casey")
driver.find_element_by_xpath("//input[@name = 'password']").send_keys("Ekata!@#$5")
driver.find_element_by_xpath("//button[@type = 'submit']").click()
# driver.find_element_by_xpath("//a[@href = '/player/']").click()
# driver.find_element_by_xpath("//input[@name = 'name']").send_keys("Bot")
# driver.find_element_by_xpath("//input[@name = 'valid_business_email']").send_keys("aashish@shorthillstech.com")
# driver.find_element_by_id("player-submit-btn").click()
time.sleep(0.3)
driver.find_element_by_xpath("//a[@href='/game/14/']").click()
time.sleep(0.3)
driver.find_element_by_id("newGameBtn").click()
time.sleep(0.3)
driver.find_element_by_id("tutPgStartGameBtn").click()
WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='tpbl-circle good-circle grow-animation-good']")))
u = 5
flaf = True

flag = True
while flaf:
    if flag == True:
        for i in range(u):
            time.sleep(0.5)
            high = driver.find_element_by_xpath("//div[@class = 'tpbl-circle good-circle grow-animation-good']")
            try:
                high.click()
            except:
                try:
                    driver.execute_script("arguments[0].click();", high)
                except:
                    pass
        time.sleep(2)
        try:
            driver.find_element_by_id("lvlPssdContinueNextLvlBtn").click()
            WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='tpbl-circle good-circle grow-animation-good']")))
        except:
            print("next level click error")
            pass
            flag = False
            flaf = False
        else:
            pass
    u = u+1











