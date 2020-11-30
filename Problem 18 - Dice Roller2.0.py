# Dice Roller 2.0
# 27 Oct 2019

from random import randint

def roll_dice(raw):
    

print("Welcome to the dice roller. Input dice to roll in the format '[# of dice)d(number of sides) + (static number)'. Ex: '4d12 + 2d10 + 4', spaces optional \nEnter 'x' when you're ready to quit.\n")
while True:
    raw = input("")
    cont = True

    # first check if it's an exit command
    if raw.lower() == "x":
        break

    # get rid of spaces, split into list on + symbol
    nonplus = raw.replace(" ", "").split("+")

    #check for errors before continuing
    for term in range(len(nonplus)):
        nonplus[term] = nonplus[term].split("d")
        if len(nonplus[term]) == 2 or len(nonplus[term]) == 1:
            for index in range(len(nonplus[term])):
                try:
                    nonplus[term][index] = int(nonplus[term][index])
                except:
                    print("Try again.\n")
                    cont = False
                    break
        else:
            print("Try again.\n")
            cont = False
            break

    # for every list in nonplus, return a single number
    static = []
    rolls = []
    if cont == True:
        for x in range(len(nonplus)):
            if len(nonplus[x]) == 1:
                static.append(int(nonplus[x][0]))
            else:
                for die in range(nonplus[x][0]):
                    rolls.append(randint(1,nonplus[x][1]))
                    
        print("You rolled a " + str(rolls) + " for a total of " + str(sum(static)+sum(rolls)) + ".\n")
                
