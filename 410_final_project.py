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
	#for link_holder in soup.find_all("span", class_="cds-143 css-v4ktz5 cds-145"): # for coursera
	for link_holder in soup.find_all("p"):
		#print(link_holder)
		extracted_text = link_holder.string #get text
		if extracted_text:
			links.append(extracted_text)
	return links

# process TF-IDF
def tfidf(dataset):
	tfIdfVectorizer=TfidfVectorizer(stop_words='english')
	tfIdf = tfIdfVectorizer.fit_transform(dataset)
	df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
	df = df[df['TF-IDF'] > .05] # filter noise 
	df = df.sort_values('TF-IDF', ascending=False)
	return df

# Extract text
url = "https://en.wikipedia.org/wiki/Go_strategy_and_tactics"
dataset = scrape_lecture_video(url,driver)
driver.close()

# Get Keywords via TF-IDF
keywords = tfidf(dataset)
print(keywords)

# Write to File
keywords.to_csv('scraped_website.csv',index=True,header=False)
# Load to HTML
