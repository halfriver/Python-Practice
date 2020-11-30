# Dice Roller 1.0
# 27 Oct 2019

from random import randint

print("Welcome to the dice roller. Input dice to roll in the format '[# of dice)d(number of sides)'. Ex: '4d12' \nEnter 'x' when you're ready to quit.\n")
while True:
    rolls = []
    dice = input("").split("d")
    if len(dice) != 2:
        if len(dice) == 1 and dice[0] == "x":
            break
        else:
            print("Try again.\n")
    else:
        try:
            dice[0] = int(dice[0])
            dice[1] = int(dice[1])
        except:
            print("Try again.\n")
        else:
            for die in range(dice[0]):
                rolls.append(randint(1,dice[1]))
            print("You rolled a " + str(rolls) + " for a total of " + str(sum(rolls)) + ".\n")
    

