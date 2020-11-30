# Countdown Timer
# 09 Nov 2019

import datetime
import time

now = datetime.datetime.now()

date_input = input("Please input the '(year) (month) (day) (hour) (minute) (second)' that you want a countdown to.\n").split(" ")
date = datetime.datetime(int(date_input[0]), int(date_input[1]), int(date_input[2]), int(date_input[3]), int(date_input[4]), int(date_input[5]))

while date > now:
    now = datetime.datetime.now()
    time.sleep(1)
    diff = date - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds - (hours * 3600)) // 60
    seconds = (diff.seconds - (hours * 3600) - (minutes * 60))
    print("Time remaining = " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")

