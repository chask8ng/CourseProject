# Project Documentation

## 1. Overview of Code
Functions scrape_lecture_video, get_js_soup:
Scrapes website to get all words from large transcripts.
Allows for downstream processing.

Function tfidf:
Produces top keywords from lecture video used, based on TF-IDF.
Allows for use of top keywords to produce on Frontend.

With these functions, you can parse any body of text to quickly identify keywords. This comes in handy when needing to find more information on topics amongst multiple documents.

## 2. Implementation
Used chromedriver to extract text from websites.
Used sklearn package to identify keywords from extracted text.

## 3. Usage of software
To install chromedriver, use the main website: https://chromedriver.chromium.org/getting-started.
After that, see this helpful guide to make sure it's connected: https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/.

## 4. Contribution
Single person team, so I did it all :)
