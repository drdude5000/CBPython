from SimpleDeck import Card

class Player:
    def __init__(self):
        #0=South 1=West 2=North 3=East
        self.designation = 0
        self.name = "Bot"
        self.points = 0
        self.handval = 0
        self.hand = []

    #Give Player 13 Cards
    #fhand should be a list of 13 card objects
    def collectHand(self, fhand):
        self.hand = fhand

    #DEBUG
    def checkHand(self):
        dout = ""
        count = 1

        for i in self.hand:
            dout = "Card " + str(count) + ": " + self.hand[count - 1].checkcard()

        return dout
