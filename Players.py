from SimpleDeck import Card

class Player:
    def __init__(self):
        #0=South 1=West 2=North 3=East
        designation = 0
        name = "Bot"
        points = 0
        handval = 0
        hand = []

    #Give Player 13 Cards
    #fhand should be a list of 13 card objects
    def giveHand(self, fhand):
        self.hand = fhand