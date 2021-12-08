# Project Documentation

## 1. Overview of Code
Functions scrape_lecture_video, get_js_soup:
Scrapes website to get all words from large transcripts.
Allows for downstream processing.

Function tfidf:
Produces top keywords from lecture video used, based on TF-IDF.
Allows for use of top keywords to produce on Frontend.

With these functions, you can parse any body of text to quickly identify keywords. 
This comes in handy when needing to find more information on topics amongst multiple documents.

Ideally wanted to do this directly against the Coursera videos, but required more permission set up. 
Example code here is to use Wikipedia instead.
The same idea, is to find keywords for lengthy articles, and make them noticeable to readers.
Then spin up keywords in a separate HTML page, since we can't edit public pages directly (generate_webpage.html file).

## 2. Implementation
Used chromedriver to extract text from websites.
Used sklearn package to identify keywords from extracted text.

## 3. Usage of software
To install chromedriver, use the main website: https://chromedriver.chromium.org/getting-started.
After that, see this helpful guide to make sure it's connected: https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/.

## 4. Contribution
Single person team, so I did it all :)

## 5. VIDEO EXPLANATION DEMO
Shared walkthrough of project here: https://drive.google.com/file/d/1Z_5aZqoJtUrOL7yy6AtaaTpPqtWW4ppK/view?usp=sharing
