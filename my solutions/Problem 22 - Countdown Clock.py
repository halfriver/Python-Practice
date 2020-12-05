# Problem 22: Countdown Timer
 # Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
 # If the selected time has already passed, have the program tell the user to start over.
 # If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.

# Original: 09 Nov 2019
# Edited: 01 December 2020

import datetime
import time
import winsound

qs = ["What year?\n",
     "What month?\n",
     "What day?\n",
     "What hour (24 hr clock)?\n",
     "What minute?\n",
     "What second?\n"]
mnth = (["jan", "january"],
        ["feb", "february"],
        ["mar", "march"],
        ["apr", "april"],
        ["may"],
        ["jun", "june"],
        ["jul", "july"],
        ["aug", "august"],
        ["sept", "september"],
        ["oct", "october"],
        ["nov", "november"],
        ["dec", "december"])
date_input = [1, 1, 1, 0, 0, 0]

def within_range(q, num):
    # if year, must be current year or later, cannot be greater than 100 years in future
    current = datetime.date.today()
    if q == 0:
        if num <= current.year+100 and num >= current.year:
            return True
        else:
            print("Please enter a year that is between now and a hundred years.")
            return False
    # month must be between 1 and 12
    elif q == 1:
        if num >= 1 and num <= 12:
            return True
        else:
            print("Please enter a valid month.")
            return False
    # day must be between 1 and 31
    elif q == 2:
        if num >= 1 and num <= 31:
            return True
        else:
            print("Please enter a valid day.")
            return False
    # hour must be between 0 and 23
    elif q == 3:
        if num >= 0 and num <= 23:
            return True
        else:
            print("Please enter a valid hour.")
            return False
    # minute and seconds must fall between 0 and 59
    else:
        if num >= 0 and num <= 59:
            return True
        else:
            print("Please enter a valid time.")
            return False
    
def is_valid(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except:
        print("This date does not exist for this given day. ")
        return False

# input handling
while True:
    for q in range(len(qs)):
        date_input[q] = 1
        while True:
            # must be ints
            x = input(qs[q]).replace(" ","")
            try:
                date_input[q] = int(x)
            except ValueError:
                # if a valid entry for month, convert to corresponding int and allow
                if q == 1:
                    for i in mnth:
                        if x.lower() in i:
                            date_input[q] = mnth.index(i)+1
                            break
                    else:
                        print("This is not a valid value. Try again.")
                        continue
                else:
                    print("This is not a valid value. Try again.")
                    continue
            
            # must be a value that is in range for its category
            if within_range(q, date_input[q]):
                if q != 2:
                    break
                # the day must be valid for the given year and month
                elif q == 2 and is_valid(date_input[0], date_input[1], date_input[2]):
                    break
    
    # must be a valid date altogether
    try:
        target = datetime.datetime(date_input[0], date_input[1], date_input[2], date_input[3], date_input[4], date_input[5])
    except:
        continue
    # cannot have already passed
    now = datetime.datetime.now()
    if target > now:
        break
    else:
        print("This time has already passed. Please input a future date and time.\n")
    
# print the countdown
while target > now:
    time.sleep(1)
    now = datetime.datetime.now()
    diff = target - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds - (hours * 3600)) // 60
    seconds = (diff.seconds - (hours * 3600) - (minutes * 60))
    if diff.days < 0:
        break
    print("Time remaining: " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")

# done, plays a beep
print("Timer done! You've reached your specified date/time!")
for i in range(3):
    winsound.Beep(2500, 1000)


