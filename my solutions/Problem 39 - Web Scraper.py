'''
Problem 39 - Web Scraper
- Make an app that scrapes the content of a website (its produced HTML code)
- The app can then check for the absence of important HTML tags for SEO,
missing alt tags on images, and whether the page has SEO meta tags
- The app can be made in various languages that support web scraping (or have a
library to do so), like Python and Java.
- Then the app can give/subtract points and create an overall score.
- You will learn:
    - How a web scraper works
    - How to traverse the HTML DOM and select elements
    - What are the important SEO tags and techniques in a web page
'''

# Original: 12 December 2020

import requests
from bs4 import BeautifulSoup
