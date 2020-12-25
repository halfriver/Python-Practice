'''
Problem 10 - Higher Lower Guessing Game
- Create a simple game where the computer randomly selects a number between 1
and 100 and the user has to guess what the number is.
- After every guess, the computer should tell the user if the guess is higher
or lower than the answer.
- When the user guesses the correct number, print out a congratulatory message.
- Add an introductory message that explains to the user how to play your game.
- In addition to the congratulatory message at the end of the game, also print
out how many guesses were taken before the user arrived at the correct answer.
- At the end of the game, allow the user to decide if they want to play again
(without having to restart the program).
- Bonus: Adjust your messages to indicate whether a guess is “much”
higher/lower, higher/lower, or “slightly” higher/lower.
'''

# Original: 16 Sept 2019
# Edited: 25 November 2020

from random import randint


# print too high or too low
def higher_lower(guess, num, guesscount):
    if int(guess) > num:
        print("Too high!")
    elif int(guess) < num:
        print("Too low!")
    else:
        print("Correct! You got the answer in " + str(guesscount) + " guesses!")


print("Welcome to the high-lower guessing game! We'll come up with a random number between 1 and 100 and you'll try to figure out what it is.")
while True:
    g_count = 0
    num = randint(1, 100)
    while True:
        while True:
            guess = input("So, what's your guess?\n").replace(" ", "")
            try:
                int(guess)
            except ValueError:
                print("That's not a valid guess. Try again.\n").replace(" ", "")
            else:
                if int(guess) in range(101):
                    break
                else:
                    print("That's not a valid guess. Try again.\n").replace(" ", "")
        g_count += 1
        higher_lower(guess, num, g_count)
        if int(guess) == num:
            break
    if input("Would you like to play again? Type Y for yes or N for no.\n").lower() == "n":
        print("Thanks for playing! Goodbye!")
        break
