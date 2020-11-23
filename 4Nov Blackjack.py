# Blackjack
# 4 Nov 2019

from random import randint
from Deck import Deck

print("Welcome to 21.")
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
        cont = input("Stay or Hit?\n").lower()
        if cont == "stay":
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

    # play again?
    again = input("Would you like to play again? Yes or no?\n").lower()
    if again == "no":
        break
    mydeck.shuffle()
    
   
