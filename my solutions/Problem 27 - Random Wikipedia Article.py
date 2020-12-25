'''
Problem 27 - Random Wikipedia Article
- Create a program that pulls titles from the official Wikipedia API and then
asks the user one by one if he or she would like to read about that article.
- Example: If the first title is Reddit, then the program should ask something
along the lines of "Would you like to read about Reddit?" If the user says yes,
then the program should open up the article for the user to read.
- Subgoals:
  - Make the program pause once the user has selected an article to read, and
  allow him or her to continue browsing different article titles once finished
  reading.
  - Allow the user to simply press ENTER to be asked about a new article.
'''

# Original: 7 December 2019
# Edited: 29 November 2020

import urllib.request
import json
import pprint
import webbrowser

# repeatability over new articles once first list of 10 is exhausted
while True:
    # grab the contents from the url, turn the json string into a python object
    contents = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json").read()
    grab = json.loads(contents)

    # make the output legible for debugging/basic parsibility purposes
    '''
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(grab)
    '''

    # iterate through and grab data
    num = []
    title = []
    for article in grab["query"]["random"]:
        num.append(str(article["id"]))
        title.append(article["title"])

    # for each title in the list, ask the user if they'd like to read
    for x in range(len(title)):
        if input("Enter 'y' if you would like to read about " + title[x] + ".\nEnter any other key to skip to next.\n").lower() == "y":
            webbrowser.open("https://en.wikipedia.org/wiki?curid=" + num[x])

    # continue or exit
    if input("10 more random articles? Enter 'y' to continue.\n").lower() != "y":
        break
