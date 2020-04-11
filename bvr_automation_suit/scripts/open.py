from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
url = "https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/"

driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//input[@type = 'email']").send_keys("aashishsaini75@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='password']").send_keys("Helloone1@123")
driver.find_element_by_id("passwordNext").click()