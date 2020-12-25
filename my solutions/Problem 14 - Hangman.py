'''
Problem 14 - Hangman
- Create a program that selects a random word and then allows the user to guess
it in a game of hangman.
- Like the real game, there should be blank spots for each letter in the word,
and a part of the body should be added each time the user guesses a letter than
is not in the answer.
- You may choose how many wrong guesses the user can make until the game ends.
- If the player loses, print out the word at the end of the game.
- Give the player the option of replaying or quitting.
'''

# Original: 14 Oct 2019
# Edited: 27 November 2020

from random import choice

# dictionary of words
f = open("inputfiles/P14-dictionary.txt", "r")
choices = f.read().split()
f.close()

print("Welcome to the game. I'll come up with a word, you guess what the word is letter by letter. Every time you guess a word that's wrong or guess a letter that's not in the word, you get closer to getting hanged! Good luck and have fun!\n")
# loop for repeatability
while True:
    # visuals
    body_comp = ["o", "|", "\\", "/", "/", "\\"]
    body = [" ", " ", " ", " ", " ", " "]
    gallows = "    ____ \n   |    | \n   |    " + body[0] + "\n   |   " + body[2] + body[1] + body[3] + "\n   |    " + body[1] + "\n   |   " + body[4] + " " + body[5] + "\n  _|_ \n |   |______ \n |          | \n |__________|"

    # use a random word from the dictionary txt file
    word = choice(choices)

    # meat of the game
    word_dict = {}
    status = ""
    stat_temp = []
    for letter in range(len(word)):
        status += "_ "
        if word[letter] in word_dict:
            word_dict[word[letter]].append(letter)
        else:
            word_dict[word[letter]] = [letter]
    wrong = []
    penalty = 0
    while True:
        # input handling
        while True:
            guess = input("Guess a letter. Or, if you feel lucky, guess the word.\n").lower()
            if guess.isalpha():
                if len(guess) != 1 and len(guess) < 5:
                    print("If you're not guessing the word, then you must enter single letters.")
                    continue
                break
            else:
                print("This is not a valid guess. Try again.")

        # if the guess is incorrect
        if ((len(guess) == 1 and guess not in word) or (len(guess) > 1 and guess != word)) and guess not in wrong:
            wrong.append(guess)
            body[penalty] = body_comp[penalty]
            gallows = "    ____ \n   |    | \n   |    " + body[0] + "\n   |   " + body[2] + body[1] + body[3] + "\n   |    " + body[1] + "\n   |   " + body[4] + " " + body[5] + "\n  _|_ \n |   |______ \n |          | \n |__________|"
            penalty += 1
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")
        # if the guess is correct
        elif len(guess) == 1 and guess in word and guess not in status:
            stat_temp = status.split()
            for value in word_dict[guess]:
                stat_temp[value] = word[value]
            status = " ".join(stat_temp)
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")
        # if the guess has already been made
        elif guess in status or guess in wrong:
            print("You've already guessed that one.\n")
        # if the guess is the word
        elif guess == word:
            status = " ".join(list(word))
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")

        # win and lose conditions
        if status.replace(" ", "") == word:
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\nCongrats! You've survived!\n")
            break
        elif body == body_comp:
            print("Whoops, you died! \nThe correct answer was " + word + ". Better luck next time.")
            break
    if input("Would you like to play again? Type 'Y' or 'N'.\n").lower() == "n":
        break
