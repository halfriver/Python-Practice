# Problem 15: War Card Game
 # War (also known as Battle in the United Kingdom) is a card game typically played by two players using a standard playing card deck. The objective of the game is to win all of the cards.
 # The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.
 # If the two cards played are of equal value, then there is a "war". Both players place the next three cards of their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards.
 # Whoever collect the 52 cards first is declared the winner.
 # Create a "Replay" option.

# Original: 5 December 2020

from inputfiles.Deck import Deck

mydeck = Deck()
mydeck.shuffle()

