from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re 
import urllib
import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#create a webdriver object and set options for headless browsing
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

#uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url,driver):
	driver.get(url)
	res_html = driver.execute_script('return document.body.innerHTML')
	soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
	return soup

#extracts all Lecture text from video page
def scrape_lecture_video(url,driver):
	links = []
	#execute js on webpage to load listings on webpage and get ready to parse the loaded HTML 
	soup = get_js_soup(url, driver)
	for link_holder in soup.find_all("span", class_="cds-143 css-v4ktz5 cds-145"): #get list of all <div> of class 'name'
		print(link_holder)
		extracted_text = link_holder.string #get text
		print(extracted_text)
		links.append(extracted_text)
	return links

# extract coursera text
url = 'https://www.coursera.org/learn/cs-410/lecture/PyTkW/lesson-5-2-feedback-in-vector-space-model-rocchio' 
#url of Coursera page to scrape
dataset = scrape_lecture_video(url,driver)
driver.close()

# process TF-IDF
tfIdfVectorizer=TfidfVectorizer(stop_words='english')
tfIdf = tfIdfVectorizer.fit_transform(dataset)
df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df[df['TF-IDF'] > .05] # filter noise 
df = df.sort_values('TF-IDF', ascending=False)
print (df.head(25))

# pretty output
# persist on page/hover