# Problem 1 - 99 Bottles
 # Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
 # Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
 # Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

# Original: 1 Sept 2019
# Edited: 24 November 2020

bottlenum = 99
def plural(x):
    if x != 1:
        return(str(x) + " bottles ")
    else:
        return(str(x) + " bottle ")
while bottlenum > 0:
    print(plural(bottlenum) + "of beer on the wall, " + plural(bottlenum) + "of beer. Take one down and pass it around. " + plural(bottlenum - 1) + "of beer on the wall.")
    bottlenum -= 1
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
    
 
