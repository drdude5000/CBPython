from SimpleDeck import BDeck
from Players import Player

#enables prints at certain debug levels 0=off 1=on
verbose = 1

#The object that will commence the game
class GameStart:
    def __init__(self):
        self.gamedeck = BDeck()
        self.gamedeck.shuffle()

        if verbose == 1:
            print(self.gamedeck.checktop())

        #Create Players
        self.playerlst = []
        for i in range(4):
            self.playerlst.append(Player())
            self.playerlst[i].designation = i
            self.playerlst[i].collectHand(self.gamedeck.giveHand())

bgame = GameStart()
print(bgame.playerlst[0].checkHand())