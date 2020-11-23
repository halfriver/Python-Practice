# 14 Oct 2019
# Hangman

import random

# dictionary of words
f = open("dictionary.txt", "r")
choices = f.read().split()

print("Welcome to the game. I'll come up with a word, you guess what the word is letter by letter. Every time you guess a word that's wrong or guess a letter that's not in the word, you get closer to getting hanged! Good luck and have fun!\n")
# loop for repeatability
while True:
    # visuals
    body_comp = ["o", "|", "\\", "/", "/", "\\"]
    body = [" ", " ", " ", " ", " ", " "]
    gallows = "    ____ \n   |    | \n   |    " + body[0] + "\n   |   " + body[2] + body[1] + body[3] + "\n   |    " + body[1] + "\n   |   " + body[4] + " " + body[5] + "\n  _|_ \n |   |______ \n |          | \n |__________|"

    # use a random word from the dictionary txt file
    word = random.choice(choices)

    # meat of the game
    word_dict = {}
    status = ""
    stat_temp = []
    for letter in range(len(word)):
        status = status + "_ "
        if word[letter] in word_dict:
            word_dict[word[letter]].append(letter)
        else:
            word_dict[word[letter]] = [letter]
    wrong = []
    penalty = 0
    while True:
        guess = input("Guess a letter. Or, if you feel lucky, guess the word.\n")
        if ((len(guess) == 1 and guess.lower() not in word) or (len(guess) > 1 and guess.lower() != word)) and guess.lower() not in wrong:
            wrong.append(guess)
            body[penalty] = body_comp[penalty]
            gallows = "    ____ \n   |    | \n   |    " + body[0] + "\n   |   " + body[2] + body[1] + body[3] + "\n   |    " + body[1] + "\n   |   " + body[4] + " " + body[5] + "\n  _|_ \n |   |______ \n |          | \n |__________|"
            penalty += 1
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")
        elif guess.lower() in wrong:
            print("You've already guessed that one. Incorrectly.\n")
        elif len(guess) == 1 and guess.lower() in word and guess.lower() not in status:
            stat_temp = status.split()
            for value in word_dict[guess.lower()]:
                stat_temp[value] = word[value]
            status = " ".join(stat_temp)
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")
        elif guess.lower() in status:
            print("You've already guessed that one.\n")
        elif guess.lower() == word:
            status = " ".join(list(word))
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\n")
        if status.split() == list(word):
            print(gallows, status, "\nBad guesses: " + str(wrong) + "\nCongrats! You've survived!\n")
            break
        if body == body_comp:
            print("Whoops, you died! \nThe correct answer was " + word + ". Better luck next time.")
            break
    cont = input("Would you like to play again? Type Yes or No.\n")
    if cont.lower() == "no":
        break
