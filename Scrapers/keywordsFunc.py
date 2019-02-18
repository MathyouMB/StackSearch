from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

def getKeyWords(link, key_terms):
    browser = webdriver.Chrome(executable_path='C:/Users/Soumen/Desktop/Programming/Selenium Drivers/chromedriver.exe')

    browser.get(link)
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='jobsearch-JobComponent-description icl-u-xs-mt--md']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
        return []
    title = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/h3").text
    company = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[1]").text
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

    with open('formattedData1.json') as f:
        data = json.load(f)
        newData = {}
        for keys,vals in data.items():
            newData[keys] = vals
            print(newData)

    """f = open('formattedData1.json','r')
    data = json.loads(f)
    newData = {}
    for keys,vals in data.items():
        newData[keys] = vals
    f.close()"""

    print(newData)
    data[title] = [company,link,keywords]
    with open('formattedData1.json', 'w') as fw:
        json.dump(data, fw)



    return keywords
key_terms = ["python", "java", "javascript", " c ", " c,", "/c", "c/", "c#", "c++", "ruby", "html", "html5", "maya", "sql", "mysql", "nosql", "arduino", "mongodb", "angular", "rails", "react", "django", ".net", "node", "assembly"]
getKeyWords("https://ca.indeed.com/viewjob?jk=1b02777c5ee5fa67&tk=1d3ts2ipc40sp803&from=serp&vjs=3",key_terms)
