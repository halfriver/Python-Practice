# Problem 39: Web Scraper/Analyzer
 # Make an app that scrapes the content of a website (it's produced HTML code)
 # The app can then check for the absence of important HTML tags for SEO, missing alt tags on images, and whether the page has SEO meta tags
 # The app can be made in various languages that support web scraping (or have a library to do so), like Python and Java.
 # Then the app can give/subtract points and create an overall score.

# Original: 12 December 2020

import requests
from bs4 import BeautifulSoup

