from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def getKeyWords(link, key_terms):
    browser = webdriver.Chrome(executable_path='C:/Users/Soumen/Desktop/Programming/Selenium Drivers/chromedriver.exe')

    browser.get(job.get_attribute("href"))
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='jobsearch-JobComponent-description icl-u-xs-mt--md']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
        return []
    # search for key words
    word_elements = browser.find_elements_by_xpath("//p")
    words = ""
    for x in word_elements:
        words += " "+x.text
    # search through description for key words
    keywords = []
    for i in range(len(key_terms)):
        if i >= 3 and i <= 6:
            if key_terms[i] in words.lower():
                keywords.append("c")
        else:
            if key_terms[i] in words.lower():
                keywords.append(key_terms[i])
    browser.quit()
    return keywords

key_terms = ["python", "java", "javascript", " c ", " c,", "/c", "c/", "c#", "c++", "ruby", "html", "html5", "maya"]

# open chrome incognito
option = webdriver.ChromeOptions()
#option.add_argument(" — incognito")

# new instance of chrome
"""
change below
"""
browser = webdriver.Chrome(executable_path='C:/Users/Soumen/Desktop/Programming/Selenium Drivers/chromedriver.exe')

# making a request:
"""
change below
"""
browser.get("https://ca.indeed.com/jobs?q=software+developer&l=Ottawa%2C+ON")
# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='jobsearch-SerpJobCard row result clickcard']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# making a response:

#titles and links
# find_elements_by_xpath returns an array of selenium objects.
title_elements = browser.find_elements_by_xpath("//a[@class='jobtitle turnstileLink']")
company_elements = browser.find_elements_by_xpath("//a[@class='turnstileLink']")
companies = [x.text for x in company_elements]
counter = 0
jobInfo = {} # title: [company, link, [keywords]]
for job in title_elements:
    jobInfo[job.text] = [companies[counter], job.get_attribute("href"), getKeyWords(job.get_attribute("href"),key_terms)]
    counter += 1
browser.quit()

for job in jobInfo.keys():
    print("Job: "+job+"\nCompany: ",jobInfo[job][0],"\nKeywords: ",jobInfo[job][2])
