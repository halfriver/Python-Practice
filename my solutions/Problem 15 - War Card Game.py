# Problem 15: War Card Game
 # War (also known as Battle in the United Kingdom) is a card game typically played by two players using a standard playing card deck. The objective of the game is to win all of the cards.
 # The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.
 # If the two cards played are of equal value, then there is a "war". Both players place the next three cards of their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards.
 # Whoever collect the 52 cards first is declared the winner.
 # Create a "Replay" option.

# Original: 5 December 2020

# note: remove/comment out all input and sleep functions to see the game run without any interruptions
from inputfiles.Deck import Deck
from time import sleep

def war(deck1, deck2, down1, down2):
    # if there are no more cards in deck from which to draw, auto lose
    if len(deck1)==0 or len(deck2)==0:
        return deck1, deck2
    
    # draw top and down cards and remove them from decks
    for i in range(3):
        if len(deck1)==1:
            break
        down1.append(deck1.pop(0))
    for i in range(3):
        if len(deck2)==1:
            break
        down2.append(deck2.pop(0))
    top1 = deck1.pop(0)
    top2 = deck2.pop(0)
    
    # prompt user for some interactivity
    input("On to battle!")
    sleep(0.5)
    
    # print stakes
    print("On the table you put down:")
    for i in range(len(down1)):
        print("  a" + down1[i][0])
    print("On top, you put forth a" + top1[0] + " to challenge.\n")
    sleep(0.5)
    print("Your opponent puts down:")
    for i in range(len(down2)):
        print("  a" + down2[i][0])
    print("and reveals a" + top2[0] + " on top.\n")
    sleep(0.5)

    # compare tops, declare winner
    if top1[1] > top2[1]:
        deck1 += [top1, top2] + down1 + down2
        print("You win this battle! You take all! Your deck now has a total of " + str(len(deck1)) + " cards.\n")
        return deck1, deck2
    elif top1[1] < top2[1]:
        deck2 += [top1, top2] + down1 + down2
        print("Your opponent wins this time! Your deck now has a total of " + str(len(deck1)) + " cards.\n")
        return deck1, deck2
    else:
        # match again, with higher stakes
        print("It's war again! The stakes grow!\n")
        down1.append(top1)
        down2.append(top2)
        return war(deck1, deck2, down1, down2)
    
print("Welcome to the War card game. You and your opponent split a deck and play to win the entire deck, card by card. It's a very tedious game based entirely off of luck.")
input("\nEnter any key to play.\n")

# repeatable game
while True:
    # game setup: divide deck in two
    fulldeck = Deck()
    mydeck = [fulldeck.draw() for card in range(26)]
    opdeck = [fulldeck.draw() for card in range(26)]

    # repeat main gameplay
    while True:
        # prompt user for some interactivity
        sleep(0.5)
        input("Start Round")
        sleep(0.5)
        # reveal top card, declare winner, winner shuffles top card to bottom
        mytop = mydeck.pop(0)
        optop = opdeck.pop(0)
        print("You flip the top card of your deck to reveal a" + mytop[0] + ", and your opponent shows a" + optop[0] + ".")
        sleep(0.5)
        if mytop[1] > optop[1]:
            mydeck.extend([mytop, optop])
            print("You win! You take the cards and now have a total of " + str(len(mydeck)) + " cards.\n")
        elif mytop[1] < optop[1]:
            opdeck.extend([mytop, optop])
            print("Your opponent wins! You now have a total of " + str(len(mydeck)) + " cards.\n")
        else:
            mydown = [mytop]
            opdown = [optop]
            print("This means War!\n")
            mydeck, opdeck = war(mydeck, opdeck, mydown, opdown)

        if len(opdeck)==0:
            print("Congratulations! You captured all of the cards. You win!\n")
            break
        elif len(mydeck)==0:
            print("You have no more cards in your deck. Your opponent wins this time.\n")
            break

    # play again?
    if input("Would you like to play again? 'Y' for yes, 'N' for no.\n").replace(" ", "").lower() in ["no", "n"]:
        print("Thank you for playing!")
        break

