import bs4 as bs
import urllib.request as request
from time import*
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import string
from random import gauss
import random
import io


browser = webdriver.Chrome("C:/PythonPractice/chromedriver.exe")
url = input("Say url:")
key_terms = ["python", "java", "javascript", " c ", " c,", "/c", "c/", "c#", "c++", "ruby", "html", "html5", "maya", "sql", "mysql", "nosql", "arduino", "mongodb", "angular", "rails", "react", "django", ".net", "node", "assembly"]


def newJob(url):
    browser.get(url)
    jobInfo = {} 
    print(browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/h3").text)
    print(browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[1]").text)
    title = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/h3").text

    print(getKeyWords(url,key_terms))
    #skills
    #company
    #name
    #link

def getKeyWords(url, key_terms):
    browser.get(url)
    # search for key words
    sleep(10)
    word_elements = browser.find_elements_by_xpath("//p")
    print(url)
    print(word_elements)
    words = ""
    for x in word_elements:
        words += " "+x.text

    print(words)
    # search through description for key words
    keywords = []
    for i in range(len(key_terms)):
        if i >= 3 and i <= 6:
            if key_terms[i] in words.lower():
                keywords.append("c")
        else:
            if key_terms[i] in words.lower():
                keywords.append(key_terms[i])
    #browser.quit()
    return keywords

while url != 'q':
    f = open("formattedData.json",'a')
    newJob(url)
   # f.write(newJob(url))
    url = input("Say url:")



def copySource(url): #converts a page source to a string based on a url
	sourceCode = browser.page_source
	return sourceCode

def switchTabSource(url):
	browser.get(url)
	sleep(5)	
	#Wait till the browser has loaded, then take the source code of the loaded page
	sourceCode = copySource(browser.current_url)
	return sourceCode