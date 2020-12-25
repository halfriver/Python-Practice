'''
Problem 24a - Variation of 21
In this project, you will make a game similar to Blackjack. In this version:
- There is only one player.
- There are two types of scores: the game score and the round score.
- The game score will begin at 100, and the game will last for five rounds.
- At the beginning of the round, print the round number. The player is given
two random cards from a deck and they will be added together to make the
player's round score.
- From here, the player has two options - draw another card to try to get their
round score closer to 21, or they can end the round.
- The player can draw as many cards as they want until they end the round or
their round score exceeds 21.
- At the end of the round, the difference between 21 and the round score is
subtracted from the game score, and then the next round begins.
- After the five rounds, the player is given their total score and the game is
over.
- Since this is a text base game, tell the user what is happening. For example,
tell him/her when s/he draws a card, the name of the card, when they bust, etc.
- Other Information About The Game
  - Aces are only worth 1.
  - All face cards are worth 10.
  - If a player busts, 21 is subtracted from their total score.
- Subgoals:
  - Create a ranking system at the end of the game and tell the user their
  rank. For example, if the player finishes with 50-59 points they get an F,
  60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
  - At the end of each round, print out the user's total score.
  - Make sure the deck has 4 of each type of card, and then remove cards as
  they are drawn. At the end of each round, make the deck have all of the cards
  again.
'''

# Original: 4 December 2020

from inputfiles.Deck import Deck
from time import sleep

print("Welcome to 21. Each game has 5 rounds. Your objective is to get as close to 21 points without going over.\n")
mydeck = Deck()

# repeatable game
while True:
    # game setup
    game_score = 100
    round_num = 1
    # total of 5 rounds per game
    while round_num < 6:
        # round reset, player starts with 2 cards
        print("Round: " + str(round_num))
        mydeck.shuffle()
        player_cards = []
        round_score = 0
        for x in range(2):
            player_cards.append(mydeck.draw())
            round_score += player_cards[x][1]
        print("Your cards are a" + player_cards[0][0] + " and a" + player_cards[1][0] + " for a total of " + str(round_score) + " points.\n")

        # rinse and repeat until the player stops drawing cards or the player reaches 21 or higher
        while True:
            cont = input("Draw 'D' or Stop 'S'?\n").replace(" ", "").lower()
            if cont in ["stop", "s"]:
                break
            elif cont in ["draw", "d"]:
                player_cards.append(mydeck.draw())
                round_score += player_cards[(len(player_cards)-1)][1]
                print("\nYou drew a" + player_cards[(len(player_cards)-1)][0] + ". Your point total is now " + str(round_score) + ".")
                if round_score >= 21:
                    break
            else:
                print("\nPlease try again:")

        # once the player finishes drawing, figure out if they won or not
        if round_score > 21:
            print("Sorry, that's a bust!\n")
            game_score -= 21
        elif round_score < 21:
            print("Close but not quite!\n")
            game_score -= 21 - round_score
        elif round_score == 21:
            print("Congrats! You got to 21 exactly!\n")

        round_num += 1
        sleep(1.5)

    # end of game ranking
    if game_score >= 90:
        ranking = "A"
    elif game_score >= 80:
        ranking = "B"
    elif game_score >= 70:
        ranking = "C"
    elif game_score >= 60:
        ranking = "D"
    else:
        ranking = "F"
    print("GAME OVER \nFinal Score: " + str(game_score) + "\nPerformance: " + ranking)

    # play again?
    if input("\nWould you like to play again? 'Y' for yes or 'N' for no.\n").replace(" ", "").lower() in ["n", "no"]:
        break
