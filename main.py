print("Welcome to the GACHA SIMULATOR where you can experience the chance based system firsthand.")
#not called Gacha Simulator, temporary placeholder until better name is found.

import random

class GachaGame:
    def __init__(self):
        self.pool = ["Item1", "Item2", "Item3", "Item4", "Item5"]
        self.pity_counter = 0
        self.pity_threshold = 50

    def pull(self):
        if self.pity_counter >= self.pity_threshold:
            item = self.pool[-1]  # Guaranteed item after reaching pity threshold
            self.pity_counter = 0
        else:
            item = random.choice(self.pool)
            self.pity_counter += 1

        return item


game = GachaGame()
for _ in range(10):
    item = game.pull()
    print("You obtained:", item)


print("This game will be difficult at first but then possible solutions will be presented to solve the issues at hand.")
#issues at hand hinting at possible gacha related issues, i.e: debt, gambling, wasteful spending, scamming.

#pick 6 types of gacha games to work on. 3 with janky mechanics and drop rates along with low payout in currency with high bundle prices. 
#3 with a pity system and good payout in currency regardless of the payout amount.
#create percentages and pull amounts based on likelyhood of getting said top tier character.
#probablity rate of 0.2% to 100%