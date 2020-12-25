'''
Problem 28 - What's the Weather?
- Create a program that pulls data from OpenWeatherMap.org and prints out
information about the current weather, such as the high, the low, and the
amount of rain for wherever you live.
- Print out data for the next 5-7 days so you have a 5 day/week long forecast.
- Print the data to another file that you can open up and view at, instead of
viewing the information in the command line.
- If you know html, write a file that you can print information to so that your
project is more interesting.
'''

# Original: 28 November 2019
# Edited: 09 December 2020

import urllib.request
import json
import pprint
import webbrowser
import os


def celsius(kelvin):
    return(round(kelvin - 273.15))


def fahren(kelvin):
    return(round((celsius(kelvin)*(9/5)) + 32))


APIkey = "8a0a2c2ff1a604ae8f89026e2091be16"
zipcode = input("Enter your ZIP code (US).\n")
url = "https://api.openweathermap.org/data/2.5/forecast?zip=" + str(zipcode) + ",us&appid=" + APIkey

# grab the contents from the url, turn the json string into a python object
contents = urllib.request.urlopen(url).read()
grab = json.loads(contents)

# make the output legible for debugging/basic parsibility purposes
'''
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(grab)
'''

# iterate through and grab data
date = []
temp = []
descript = []
for timepoint in grab["list"]:
    date.append(timepoint["dt_txt"])
    temp.append(timepoint["main"]["temp"])
    descript.append(timepoint["weather"][0]["main"])

# split data into each day, find temp max/min and general weather description for each day
final = {}
day_temp = []
day_descript = []
for dt in range(len(date)):
    date[dt] = date[dt].split(" ")[0]
    # if new day, create new dictionary in final for that day
    if date[dt] not in final:
        final[date[dt]] = {}
        # if there's data stored from previous day, enter previous day's data into final and clear lists
        if len(day_temp) > 0:
            final[date[dt-1]]["hitemp_c"] = celsius(max(day_temp))
            final[date[dt-1]]["lotemp_c"] = celsius(min(day_temp))
            final[date[dt-1]]["hitemp_f"] = fahren(max(day_temp))
            final[date[dt-1]]["lotemp_f"] = fahren(min(day_temp))
            final[date[dt-1]]["description"] = day_descript
            day_temp = []
            day_descript = []
    # if not new day, then just proceed and append data to daily list
    day_temp.append(temp[dt])
    if descript[dt] not in day_descript:
        day_descript.append(descript[dt])
    # if it's the last iteration, then append the data from the current day
    if len(date)-1 == dt:
        final[date[dt-1]]["hitemp_c"] = celsius(max(day_temp))
        final[date[dt-1]]["lotemp_c"] = celsius(min(day_temp))
        final[date[dt-1]]["hitemp_f"] = fahren(max(day_temp))
        final[date[dt-1]]["lotemp_f"] = fahren(min(day_temp))
        final[date[dt-1]]["description"] = day_descript

# make it spit out something pretty
html_opening = """
<!DOCTYPE html>
<html>
<head>
  <style>
      table, th, td {border: 1px solid black !important;}
  </style>
</head>
<body>
"""
html_body = """
<table style="width:100%">
  <tr>
"""
html_closing = """
</table>
</body>
</html>
"""

# fill in table by day, each day takses up a column
lotemp = "\n  <tr>"
hitemp = "\n  <tr>"
weather = "\n  <tr>"
count = 0
for day in final:
    html_body = html_body + "\n    <th>" + day + "</th>"
    lotemp += "\n    <td style=\"color:blue;\">Low: " + str(final[day]["lotemp_c"]) + "°C (" + str(final[day]["lotemp_f"]) + "°F)</td>"
    hitemp += "\n    <td style=\"color:red;\">High: " + str(final[day]["hitemp_c"]) + "°C (" + str(final[day]["hitemp_f"]) + "°F)</td>"
    weather = weather + "\n    <td>"
    for x in range(len(final[day]["description"])):
        weather = weather + final[day]["description"][x]
        if x != len(final[day]["description"])-1:
            weather += ", "
    weather = weather + "</td>"
    count += 1
    if count == 6:
        html_body = html_body + "\n  </tr>"
        lotemp += "\n  </tr>"
        hitemp += "\n  </tr>"
        weather += "\n  </tr>"
html_body = html_body + weather + lotemp + hitemp

html_file = open("outputfiles/P28-5DayWeather.html", "w")
html_file.write(html_opening + html_body + html_closing)
html_file.close()

# open html displaying results in browser
webbrowser.open("file://" + os.path.realpath("outputfiles/P28-5DayWeather.html"))

print("The 5-day weather forecast for " + zipcode + " has been printed to P28-5DayWeather.html in this same directory. :)")
