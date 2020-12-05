# Problem 15: War Card Game
 # War (also known as Battle in the United Kingdom) is a card game typically played by two players using a standard playing card deck. The objective of the game is to win all of the cards.
 # The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.
 # If the two cards played are of equal value, then there is a "war". Both players place the next three cards of their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards.
 # Whoever collect the 52 cards first is declared the winner.
 # Create a "Replay" option.

# Original: 5 December 2020

from inputfiles.Deck import Deck
from time import sleep

def war(deck1, deck2, down1, down2):
    # draw top and down cards and remove them from decks
    for i in range(3):
        print(deck1[0], deck2[0])
        down1.append(deck1[0])
        down2.append(deck2[0])
        deck1.remove(deck1[0])
        deck2.remove(deck2[0])
    top1 = deck1[0]
    top2 = deck2[0]
    deck1.remove(top1)
    deck2.remove(top2)
    # prompt user for some interactivity
    
    # compare tops
    print("You put down a" + down1[0][0] + ", a" + down1[1][0] + ", and a" + down1[2][0] + ". On top, you put forth a" + top1[0] + " to challenge.",
          "Your opponents lays down a" + down2[0][0] + ", a" + down2[1][0] + ", and a" + down2[2][0] + ", and reveals a" + top2[0] + " on top.")
    if top1[1] > top2[1]:
        print("You win this battle! You take all! Your deck now has a total of " + str(len(deck1)) + ".\n")
        deck1.extend([top1, top2, down1, down2])
        return deck1, deck2
    elif top1[1] < top2[1]:
        print("Your opponent wins this time! Your deck now has a total of " + str(len(deck1)) + ".\n")
        deck1.extend([top1, top2, down1, down2])
        return deck1, deck2
    else:
        # match again, with higher stakes
        print("It's war again! The stakes grow!\n")
        down1.append(top1)
        down2.append(top2)
        war(deck1, deck2, down1, down2)
    
print("Welcome to the War card game. You and your opponent split a deck and play to win the entire deck, card by card. It's a very tedious game based entirely off of luck.")
input("\nEnter any key to play.\n")
fulldeck = Deck()

# repeatable game
while True:
    # game setup: divide deck in two
    mydeck = []
    opdeck = []
    for card in range(52//2):
        mydeck.append(fulldeck.draw())
        opdeck.append(fulldeck.draw())

    # repeat main gameplay
    while True:
        # reveal top card, declare winner, winner shuffles top card to bottom
        mytop = mydeck[0]
        optop = opdeck[0]
        mydeck.remove(mytop)
        opdeck.remove(optop)
        print("You flip the top card of your deck to reveal a" + mytop[0] + ", and your opponent shows a " + optop[0] + ".")
        if mytop[1] > optop[1]:
            mydeck.extend([mytop, optop])
            print("You win! You take the cards and now have a total of " + str(len(mydeck)) + ".\n")
        elif mytop[1] < optop[1]:
            opdeck.extend([mytop, optop])
            print("Your opponent wins! You now have a total of " + str(len(mydeck)) + ".\n")
        else:
            mydown = []
            opdown = []
            mydown.append(mytop)
            opdown.append(optop)
            print("This means war!")
            
            mydeck, opdeck = war(mydeck, opdeck, mydown, opdown)
            
        if len(mydeck)==52 or len(opdeck)==52:
            break

    # play again?
    if input("Would you like to play again? 'Y' for yes, 'N' for no.\n").replace(" ", "").lower() in ["no", "n"]:
        print("Thank you for playing!")
        break

        
## adjust print statements in war function to print correct down cards (it may shift)
## make sure all cards are accounted for (losing cards when running game)
## add in sleep function and line breaks to make output less horrendous
## add in more intermediate input functions to prompt the user to flip, give some interactivity to the game
## account for end-of-deck shuffling and end-game lack of cards to make full down stacks
