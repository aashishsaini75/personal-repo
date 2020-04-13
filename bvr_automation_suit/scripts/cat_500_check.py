from selenium import webdriver
prod_url = "https://bestviewsreviews.com/all/"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
dev_url = "https://dev2.bestviewsreviews.com/all/"
driver = webdriver.Chrome(executable_path="../drivers/chromedriver",chrome_options=chrome_options)
driver.get(dev_url)
driver.maximize_window()
links = []
cat = driver.find_element_by_xpath("//*[@class = 'four-division all_categories_footer']").find_elements_by_xpath("//ul[@style ='display: flex;']")
for i in cat:
    var = i.find_element_by_tag_name("a").get_attribute("href")
    links.append(var)
a=0
for j in links:
    driver.get(j)
    if  "ValueError" in driver.page_source:
        print("Error in "+j)
    else:
        if "Server Error (500)" in driver.page_source:
            print("Error in " + j)
        else:
            pass
    a= a+1
    print(a)
driver.quit()