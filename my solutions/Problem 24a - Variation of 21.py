# Problem 24b: Blackjack
 # This is a one-player variation with no dealer.
 # At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.
 # From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.
 # The player can draw as many cards as they want until they end the round or their round score exceeds 21.
 # At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over. ---Other Information About The Game---
 # Aces are only worth 1. All face cards are worth 10.
 # If a player busts, 21 is subtracted from their total score.
 # At the beginning of each round, print the round number (1 to 5).
 # Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
 # Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
 # At the end of each round, print out the user's total score.
 # Make sure the deck has 4 of each type of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.

# Original: 4 December 2020

from inputfiles.Deck import Deck

print("Welcome to 21. Each game has 5 rounds. Your options are to Stand (end round) or to Hit (draw another card).")
mydeck = Deck()

# repeatable game
while True:
    # game setup: dealer draw two, player draw one, ask for input
    player = []
    dealer = []
    player_value = 0
    dealer_value = 0
    for x in range(2):
        dealer.append(mydeck.draw())
        player.append(mydeck.draw())
        dealer_value += dealer[x][1]
        player_value += player[x][1]
    print("\nThe dealer has one card face down, one card face up. You can see a" + dealer[1][0] + ".\nYour cards are a" + player[0][0] + " and a" + player[1][0] + " for a total of " + str(player_value) + " points.\n")

    # rinse and repeat until the player stops drawing cards
    while True:
        cont = input("Stand or Hit?\n").lower()
        if cont == "stand":
            print("\nThe dealer flips the face-down card. It's a" + dealer[0][0] + " for a total of " + str(dealer_value) + " points.\n")
            break
        elif cont == "hit":
            player.append(mydeck.draw())
            player_value += player[(len(player)-1)][1]
            print("\nYou drew a" + player[(len(player)-1)][0] + ". Your point total is now " + str(player_value) + ".")
            if player_value >= 21:
                break
        else:
            print("\nPlease try again:")

    # once the player finishes drawing, figure out if they won or not
    if player_value > 21:
        print("That's a bust! Sorry, you lose!\n")
    # while the dealer is losing, they will always hit until they win or bust
    else:
        while dealer_value <= player_value and dealer_value != 21:
            dealer.append(mydeck.draw())
            dealer_value += dealer[(len(dealer)-1)][1]
            print("The dealer draws another card, a" + dealer[(len(dealer)-1)][0] + ". His total is now at " + str(dealer_value) + " points.\n")
        if dealer_value == player_value:
            print("You and the dealer both scored a " + str(dealer_value) + ". It's a draw!\n")
        elif player_value == 21:
            print("Congrats! You got exactly 21! You won!\n")
        elif dealer_value > 21:
            print("The dealer got a total score of " + str(dealer_value) + " and you got a total score of " + str(player_value) + ". You won!\n")
        elif dealer_value <= 21:
            print("The dealer got a total score of " + str(dealer_value) + " and you got a total score of " + str(player_value) + ". You lost!\n")

    # end of game: play again?
    again = input("Would you like to play again? Yes or no?\n").lower()
    if again == "no":
        break
    mydeck.shuffle()
    
   
