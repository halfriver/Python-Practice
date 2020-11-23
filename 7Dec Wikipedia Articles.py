# Wikipedia Articles
# 7 December 2019

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
        yes_no = input("Would you like to read about " + title[x] + "?\n")
        if yes_no.lower() == "yes":
            webbrowser.open("https://en.wikipedia.org/wiki?curid=" + num[x])
    cont = input("10 more random articles? Enter \"yes\" to continue.")
    if cont.lower() != "yes":
        break
