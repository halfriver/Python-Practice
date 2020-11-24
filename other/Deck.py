from random import randint


class Deck:
    
    def __init__(self):
        self.face = ["n Ace", " 2", " 3", " 4", " 5", " 6", " 7", "n 8", " 9", " 10", " Jack", " Queen", " King"]
        self.suit = [" of Hearts", " of Diamonds", " of Clubs", " of Spades"]
        self.shuffle()

    # creates a deck, each list within the deck list signifies one card, identified by 3 numbers (face, suit, value)
    def shuffle(self):
        self.deck = []
        for card in range(52):
            suit_v = (card % 4)
            face_v = (card % 13)
            if face_v > 9:
                value = 10
            else:
                value = face_v + 1
            self.deck.append([suit_v, face_v, value])

    # draw a card from the deck
    def draw(self):
        drawn = self.deck[randint(0, len(self.deck)-1)]
        temp = [x for x in drawn]
        self.deck.remove(drawn)
        return (self.face[temp[1]] + self.suit[temp[0]], temp[2])
