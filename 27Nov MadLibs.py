# MadLibs
# 27 November 2019

text = []
words = ""
a_an = []

def is_vowel(letter):
    if letter in ["a", "i", "u", "e", "o"]:
        return True

# get file input and write it to a list
fname = input("What file would you like to read from?\n")
with open(fname, "r") as f:
    text = [line for line in f]

# split and get user inputs on words to fill in, rejoin to a single string
text = text[0].replace("[", "]").split("]")
for i in range(len(text)):
    if i%2 != 0:
        words = str(input("Give me a " + text[i] + ".\n"))
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






