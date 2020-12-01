# Problem 22: Countdown Timer
 # Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
 # If the selected time has already passed, have the program tell the user to start over.
 # If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.

# Original: 09 Nov 2019
# Edited: 01 December 2020

import datetime
import time

now = datetime.datetime.now()

date_input = []
qs = ["What year?\n",
     "What month?\n",
     "What day?\n",
     "What hour (24 hr clock)?\n",
     "What minute?\n",
     "What second?\n"]

# input handling
for q in range(len(qs)):
    while True:
        # must be ints
        try:
            # month may be expressed as a number or as the name/abbreviation of the month
            if q == 1:
                print("placeholder")
            date_input.append(int(input(qs[q]).replace(" ","")))
            break
        except ValueError:
            print("This is not a valid value. Try again.")
        # cannot have already passed
        
target = datetime.datetime(int(date_input[0]), int(date_input[1]), int(date_input[2]), int(date_input[3]), int(date_input[4]), int(date_input[5]))

# print the countdown
while target > now:
    now = datetime.datetime.now()
    diff = target - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds - (hours * 3600)) // 60
    seconds = (diff.seconds - (hours * 3600) - (minutes * 60))
    print("Time remaining: " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")
    time.sleep(1)

print("Timer done! You've reached your specified date/time!")

