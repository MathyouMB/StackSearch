import bs4 as bs
import urllib.request as request
from time import*
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import string
from random import gauss
import random
import io


chrome = False
#browser = webdriver.Chrome("C:/PythonPractice/chromedriver.exe")
browser = webdriver.PhantomJS()


loginUrl = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

def login():
	#take code from page
	sourceCode = switchTabSource(loginUrl)
	#put in username
	nameBox = browser.find_element_by_xpath(formatID(findBetween(sourceCode,'Phone number, username, or email</label><input class="_2hvTZ pexuQ zyHYP" id="','" aria-label="Phone number, username,')))
	
	nameBox.send_keys(botUsername)
	#put in password
	passwordBox = browser.find_element_by_xpath(formatID(findBetween(sourceCode,'Password</label><input class="_2hvTZ pexuQ zyHYP" id="','" aria-label="Password"')))
	passwordBox.send_keys(botPassword)
	#click login button
	browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button""").click()

def copySource(url): #converts a page source to a string based on a url
	sourceCode = browser.page_source
	return sourceCode

def switchTabSource(url):
	#Switch to instagram login screen
	browser.get(url)
	testSleep(2)	
	#Wait till the browser has loaded, then take the source code of the loaded page
	sourceCode = copySource(browser.current_url)
	return sourceCode
	
def formatID(id): #formats a xpath id string
	idString = '//*[@id="'+id+'"]'
	return(idString)

def testSleep(x): #a method for telling me when im sleeping on a page
	sleep(randomize_time(x))
	#sleep(x)
def randomize_time(mean):
	allowed_range = mean * 0.5
	stdev = allowed_range / 3  
	t = 0
	while abs(mean - t) > allowed_range:
		t = gauss(mean, stdev)
	return t

def scrapeInstaPage(username):
	print("\nScrapping "+username+" -----")
	sourceCode = switchTabSource(formatProfileUrl(username))
	userInfo = getProfileInfo(sourceCode,username)
	f = open("source.txt","w", encoding="utf-8")
	#write = sourceCode.rstrip("\n\r")
	#write = write.strip()
	#write.replace("\n", " ")
	f.write(sourceCode)
	f.close()
	#picUrls = getPicUrls(sourceCode)
	#picInfo = getPicInfo(picUrls,userInfo)

	#print(*userInfo, sep='\n')
	#print(*picInfo, sep='\n')	
	
	print("\nUserInfo ------------------------------------")
	print("\nUsername: "+userInfo[0])
	print("Display Name: "+userInfo[1])
	print("Posts: "+userInfo[2])
	print("Followers: "+userInfo[3])
	print("Following: "+userInfo[4])
	print("\n[url, likes, comments, date] ----------------")
	#print(*picInfo, sep='\n')
	
	return userInfo

def getProfileInfo(sourceCode,username):
	userInfo = []
	
	
	description = findBetween(sourceCode,'meta property="og:description" content="',' - See Instagram photos and videos from')
	#description +=','
	cells = description.split(',')
	#print (cells)
	#print(description)

	postNum = (cells[2].replace(" ","")).replace("Posts","")
	followingNum = (cells[1].replace(" ","")).replace("Following","")
	followerNum = (cells[0].replace(" ","")).replace("Followers","")
	#postNum = cell[2].replace()
	#followingNum = findBetween(sourceCode,'following/"><span class="g47SY lOXF2">','</span> following</a></li></ul><div class="fx7hk">')
	#followerNum = findBetween(sourceCode,'<meta property="og:description" content="',' Followers, '+str(followingNum)+' Following, '+str(postNum)+' Posts - See Instagram photos and videos from ')
	givenName = findBetween(sourceCode,'See Instagram photos and videos from ',' (@'+username+')" name="description">')
	#print(test)

	#print("------------------------------------")
	#print("Username: "+username)
	#print("Display Name: "+givenName)
	#print(postNum+ " posts")
	#print(followerNum+ " followers")
	#print(followingNum+ " following")
	#print("------------------------------------")

	userInfo.append(username)
	userInfo.append(givenName)
	userInfo.append(postNum)
	userInfo.append(followerNum)
	userInfo.append(followingNum)

	return (userInfo)

def getPicUrls(source):
	
	#for 0-3 (1-4)
	#cut out 1 of the 4 rows
		#for 0-2 (1-3)
		#cut out 1 of the 3 photos
			#cut out the link
		#remove the photo section from the row code
	#remove the row from the overall photocode


	links = []
	photoSource = findBetween(source,'<div class=" _2z6nI">','</div></main>') #ALL PHOTOS
	tempSource = photoSource

	for j in range(0,3,1):#we take just the first 3 rows, I was too lazy to take the forth row (if I wanted to, just dont check for the <div class="Nnq7C weEfm">)
		
		photoRow = findBetween(tempSource,'<div style="flex-direction: column; padding-bottom: 0px; padding-top: 0px;">','</div><div class="Nnq7C weEfm">')
		tempRow = photoRow

		#photo1
		photo = findBetween(tempRow,'<div class="Nnq7C weEfm">','</div><div class="v1Nh3 kIKUG  _bz0w">')
		link = ("https://www.instagram.com"+findBetween(photo,'<div class="v1Nh3 kIKUG  _bz0w"><a href="','"><div class="eLAPa"><div class="KL4Bh">'))
		tempRow = str.replace(tempRow,photo+'</div>',"") #remove the photo from code
		links.append(link)
		#print(link)

		#photo2
		photo = findBetween(tempRow,'<div class="Nnq7C weEfm">','</div><div class="v1Nh3 kIKUG  _bz0w">')
		link = ("https://www.instagram.com"+findBetween(photo,'<div class="v1Nh3 kIKUG  _bz0w"><a href="','"><div class="eLAPa"><div class="KL4Bh">'))
		tempRow = str.replace(tempRow,photo+'</div>',"") #remove the photo from code
		links.append(link)
		#print(link)

		#photo3
		photo = findBetween(tempRow,'<div class="Nnq7C weEfm">','</div>')
		link = ("https://www.instagram.com"+findBetween(photo,'<div class="v1Nh3 kIKUG  _bz0w"><a href="','"><div class="eLAPa"><div class="KL4Bh">'))
		links.append(link)
		#print(link)

		#remove this row from tempsource
		tempSource = str.replace(tempSource,photoRow+'</div>',"")
	
	return (links)

def getPicInfo(picUrls,userInfo):
	picInfo = []
	for i in range(len(picUrls)):
		picInfo.append(scrapePic(picUrls[i],userInfo))
	return (picInfo)

def scrapePic(url,userInfo):
	picStats = []
	source = switchTabSource(url)
	LandC = getLandC(source,url,userInfo)
	picStats.append(url)#url
	picStats.append(LandC[0])
	picStats.append(LandC[1])
	#picStats.append(findBetween(source,'<link rel="canonical" href="'+(str.replace(url,'?taken-by='+userInfo[0],""))+'" />\n    <meta content="',' - '+userInfo[1]+' (@'+userInfo[0]+') on Instagram'))
	picStats.append(findBetween(source,'<time class="_1o9PC Nzb55" datetime="','" title="')) # date
	return picStats

def getLandC(source,url,userInfo):
	LandC = []
	s = findBetween(source,'<link rel="canonical" href="'+(str.replace(url,'?taken-by='+userInfo[0],""))+'" />\n    <meta content="',' - '+userInfo[1]+' (@'+userInfo[0]+') on Instagram')
	likes = findBetween(s,'',' Likes,')
	comments = findBetween(s,'Likes, ',' Comments')
	LandC.append(likes)
	LandC.append(comments)
	return (LandC)
def findBetween( s, first, last ):
	start_index = s.find(first)
	end_index = start_index + len(first)
	last_index = s.find(last)

	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def formatProfileUrl(name):
	url = ("https://www.instagram.com/"+name+"/")
	#print('\n------------------------------ \n'+'Scrapping '+ url+'   ('+strftime("%Y-%m-%d %H:%M:%S", gmtime())+')\n------------------------------\n')
	return(url)

def scrape(name):
	#print('instaScrape------------------------------ '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	
	login()
	#usernameInput = input("Enter a instagram username: ")
	#while usernameInput != "q":
	
		#usernameInput = input("\nEnter a instagram username: ")
	
	return (scrapeInstaPage(name))
	browser.quit()
#scrape("wilsoliama")
#driver.quit()