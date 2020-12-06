# Dice Rolling Simulator
 # Allow the user to input the amount of sides on a dice and how many times it should be rolled.
 # Your program should simulate dice rolls and keep track of how many times each number comes up.
 # Finally, print out how many times each number came up.
 # Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
 # Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
 # In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.
 
# Original: 27 Oct 2019
# Edited: 6 December 2020

from random import randint

print("Input dice to roll in the format '[# of dice)d(# of sides) + (static number)'. Example: '4d12 + 2d10 - 4', spaces not required. \nEnter 'x' when you're ready to quit.")
while True:
    dice = input("").lower().replace(" ", "")
    rolls = []
    static = []
    total = []
    out = "\n"

    # first check if it's an exit command
    if dice == "x":
        break

    # split into list of numbers (account for + and -)
    dice = dice.replace("+", " +").replace("-", " -").split()
    dice = [dice[x].split("d") for x in range(len(dice))]
    try:
        # must be ints
        dice = [[int(j) for j in dice[i]] for i in range(len(dice))]
        # must have no more than 2 terms in each sublist
        for i in dice:
            if len(i) > 2:
                raise ValueError
            # separate dice and static numbers
            elif len(i) == 1:
                static.append(i[0])
        for i in static:
            dice.remove([i])
        # remove any terms equal to 0
        for i in dice:
            if 0 in i:
                dice.remove(i)
        for i in static:
            if i == 0:
                static.remove(i)
    except ValueError:
        print("What you entered is not in the correct format (e.g., '4d12 + 2d10 - 4'). Please try again:")
        continue

    # convert dice list into random rolls
    for i in dice:
        rolls.append([randint(1, i[1]) for j in range(abs(i[0]))])

    # sum total
    for i in range(len(rolls)):
        total.append(sum(rolls[i]))
        if dice[i][0] < 0:
            total[i] *= -1
    total.append(sum(static))

    # stitch into printable statements
    for i in range(len(rolls)):
        if i != 0:
            if dice[i][0] > 0:
                out += "+"
            else:
                out += "-"
        elif i == 0 and dice[i][0] < 0:
            out += "-"
        out += "("
        for j in range(len(rolls[i])):
            out += str(rolls[i][j])
            if j != len(rolls[i])-1:
                out += "+"
        out += ")"
    if len(static) > 0:
        if sum(static) > 0:
            out += "+"
        else:
            out += "-"
        out += str(abs(sum(static)))
        
    out += "\nTotal: " + str(sum(total)) + "\n" 
    
    print(out)

## Original, only processes single inputs such as 4d12   
##    rolls = []
##    dice = input("").split("d")
##    if len(dice) != 2:
##        if len(dice) == 1 and dice[0] == "x":
##            break
##        else:
##            print("Try again.\n")
##    else:
##        try:
##            dice[0] = int(dice[0])
##            dice[1] = int(dice[1])
##        except:
##            print("Try again.\n")
##        else:
##            for die in range(dice[0]):
##                rolls.append(randint(1,dice[1]))
##            print("You rolled a " + str(rolls) + " for a total of " + str(sum(rolls)) + ".\n")
    

