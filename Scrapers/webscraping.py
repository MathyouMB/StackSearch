from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

def getKeyWords(link,currentID):
    key_terms = ["python", "java", "javascript", " c ", "c#", "c++", "ruby", "html", "html5", "maya", "sql", "mysql", "nosql", "arduino", "mongodb", "angular", "rails", "react", "django", ".net", "node", "assembly"]
    browser = webdriver.Chrome(executable_path='/Users/ericpham/Downloads/chromedriver')

    browser.get(link)
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='jobsearch-JobComponent icl-u-xs-mt--sm jobsearch-JobComponent-bottomDivider']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
        return []

    data = {}
    title = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/h3").text
    company = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[1]").text
    data[currentID+1] = [title,company,link,[]]
    currentID+= 1

    # search for key words
    words = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]").text
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
    data[title][3] = keywords
    # ID: [Job Title, Company Name, [Keywords]]

    return data
