# 16 Sept 2019
# Higher-Lower Guessing Game

from random import randint

def higher_lower(guess, num, g_count):
    if int(guess) > num:
        print("Too high!")
    elif int(guess) < num:
        print("Too low!")
    elif int(guess) == num:
        print("Correct! You got the answer in " + str(g_count) + " guesses!")

print("Welcome to the high-lower guessing game! We'll come up with a random number between 1 and 100 and you'll try to figure out what it is.") 
while True:
    g_count = 0
    num = randint(1, 100)
    while True:
        while True:
            guess = input("So, what's your guess?\n")
            try:
                int(guess)
            except ValueError:
                print("That's not a valid guess. Try again.")
            else:
                if int(guess) in range(1,101):
                    break
                else:
                    print("That's not a valid guess. Try again.")
        g_count +=1
        higher_lower(guess,num, g_count)
        if int(guess) == num:
            break
    cont = input("Would you like to play again? Type Y for yes or N for no.\n")
    if cont.lower() == "n":
        print("Thanks for playing! Goodbye!")
        break
