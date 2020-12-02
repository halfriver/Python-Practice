# Problem 7: MadLibs Story-Maker
 # Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted.
 # The story doesn't have to be too long, but it should have some sort of story line.
 # If the user has to put in a name, change the first letter to a capital letter.
 # Change the word "a" to "an" when the next word in the sentence begins with a vowel.

# Original: 27 November 2019
# Edited: 29 November 2020

text = []
words = ""
a_an = []

def is_vowel(letter):
    if letter in ["a", "i", "u", "e", "o"]:
        return True

# get file input and write it to a list
fname = "inputfiles/P07-madlibs.txt"
with open(fname, "r") as f:
    text = [line for line in f]
f.close()

# split and get user inputs on words to fill in, rejoin to a single string
text = text[0].replace("[", "]").split("]")
for i in range(len(text)):
    if i%2 != 0:
        words = str(input("Give me: " + text[i] + "\n"))
        text[i] = words
words = "".join(text)

# account for a/an changes
text = words.split(" a ")
for i in range(1,len(text)):
    if  is_vowel(text[i-1][0]) == True:
        a_an.append(" an ")
    else:
        a_an.append(" a ")
words = text[0]
for i in range(len(a_an)):
    words = words + a_an[i] + text[i+1]

print(words)






