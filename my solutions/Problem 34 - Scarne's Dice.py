'''
Problem 34 - Scarne's Dice
- Make a turn-based dice game where players compete to reach (or exceed) 100
points by rolling a die.
- Rolling a 1 scores no points and the roller loses their turn.
- Upon rolling a 2 to 6, the player can choose to either reroll or end their
turn. Ending their turn adds the number they rolled to the number of points. A
player can reroll as many times as they’d like on their turn.
'''

# Original: 10 December 2020

from random import randint


def roll():
    return randint(1, 6)


# call when player's turn
def score(num):
    if num == 1:
        print("Sorry, you rolled a 1! You lose your turn.")
        return 0
    else:
        print("You rolled a " + str(num) + ".")
        if num == 6:
            return num
        else:
            while True:
                choice = input("Would you like to try again to roll higher 'R' or would you like to end your turn now 'E'?\n").lower().strip()
                if choice == 'e':
                    return num
                elif choice == 'r':
                    return score(roll())
                else:
                    print("This was not a valid input.")


# call when opponent's turn
def opp_score(num):
    if num == 1:
        print("Your opponent rolls a 1! They lose their turn.\n")
        return 0
    else:
        print("Your opponent rolls a " + str(num) + ".\n")
        return num


# repeatable gameplay
while True:
    print("Welcome to Scarne's Dice! Your goal is to reach 100 points before your opponent.\n")
    player = 0
    opponent = 0
    r = 1
    input("Your turn first! Hit 'Enter' to start the game.\n")

    while True:
        # player's turn
        player += score(roll())
        if player >= 100:
            print("Congrats, you just reached " + str(player) + " points. You win!")
            break

        # opponent's turn
        opponent += opp_score(roll())
        if opponent >= 100:
            print("Your opponent just reached " + str(opponent) + " points. Sorry, you lose!")
            break

        r += 1
        print("Round " + str(r) + "\nScore: " + str(player) + "-" + str(opponent))
        input("")

    # play again?
    if input("Play again? Or enter 'X' to exit.").strip().lower() == 'x':
        print("Thanks for playing!")
        break
