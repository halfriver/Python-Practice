# Problem 5: Rock Paper Scissors
 # Create a rock-paper-scissors game.
 # Ask the player to pick rock, paper or scissors.
 # Have the computer chose its move.
 # Compare the choices and decide who wins. 
 # Print the results.

# Original: 24 November 2020

from random import randint
from time import sleep

options = ("Rock", "Paper", "Scissors", "r", "p", "s")
def winner(user, computer):
    # if the user picks rock and the computer picks scissors, user wins
    if user - computer == -2:
        return True
    # if the user picks scissors and the computer picks rock, user loses
    elif user - computer == 2:
        return False
    # if user > computer, user wins
    elif user > computer:
        return True
        
# score = [player, computer]
score = [0, 0]

# keep game going until user exits
while True:
    # clear plays
    computer = ""
    throw = ""
    
    # repeat until valid option is entered
    while (throw not in options):
        throw = input("Enter rock (r), paper (p), or scissors (s).\n").lower().strip()

    # determine user's play if they entered a single letter
    if options.index(throw) >= 3:
        throw = options[options.index(throw) - 3]

    # for flair
    print("Rock...")
    sleep(0.75)
    print("Paper...")
    sleep(0.75)
    print("Scissors...")
    sleep(0.75)
    print("Shoot!\n")
    sleep(0.75)
    
    # computer picks and outcome printed
    computer = options[randint(0, 2)]
    print("You throw a " + throw + " against your opponent's " + computer + ".\n")
    # if the user and computer chose the same, it's a draw
    if options.index(throw) == options.index(computer):
        print("It's a draw! The score remains " + str(score[0]) + "-" + str(score[1]) + ".")
    # if winner == True
    elif winner(options.index(throw), options.index(computer)):
        score[0] += 1
        print("You win! The score is now " + str(score[0]) + "-" + str(score[1]) + ".")
    # otherwise the computer wins
    else:
        score[1] += 1
        print("Your opponent wins this round! The score is now " + str(score[0]) + "-" + str(score[1]) + ".")

    # repeat or exit
    if input("Enter 'x' to exit, hit 'enter' to continue.\n").lower() == "x":
        break
