print("Welcome to the GACHA SIMULATOR where you can experience the chance based system firsthand.")
#not called Gacha Simulator, temporary placeholder until better name is found.

import random

class GachaGame:
    def __init__(self):
        self.pool = [
            {"name": "1", "rarity": "Common", "probability": 0.6},
            {"name": "2", "rarity": "Common", "probability": 0.6},
            {"name": "3", "rarity": "Uncommon", "probability": 0.3},
            {"name": "4", "rarity": "Uncommon", "probability": 0.3},
            {"name": "5", "rarity": "Rare", "probability": 0.1},
            {"name": "6", "rarity": "Common", "probability": 0.6},
            {"name": "7", "rarity": "Common", "probability": 0.6},
            {"name": "8", "rarity": "Uncommon", "probability": 0.3},
            {"name": "9", "rarity": "Uncommon", "probability": 0.3},
            {"name": "10", "rarity": "Rare", "probability": 0.1},
            {"name": "11", "rarity": "Common", "probability": 0.6},
            {"name": "12", "rarity": "Common", "probability": 0.6},
            {"name": "13", "rarity": "Uncommon", "probability": 0.3},
            {"name": "14", "rarity": "Uncommon", "probability": 0.3},
            {"name": "15", "rarity": "Rare", "probability": 0.1},
            {"name": "16", "rarity": "Common", "probability": 0.6},
            {"name": "17", "rarity": "Common", "probability": 0.6},
            {"name": "18", "rarity": "Uncommon", "probability": 0.3},
            {"name": "19", "rarity": "Uncommon", "probability": 0.3},
            {"name": "20", "rarity": "Rare", "probability": 0.1},
            {"name": "22", "rarity": "Common", "probability": 0.6},
            {"name": "23", "rarity": "Common", "probability": 0.6},
            {"name": "24", "rarity": "Uncommon", "probability": 0.3},
            {"name": "25", "rarity": "Uncommon", "probability": 0.3},
            {"name": "26", "rarity": "Rare", "probability": 0.1},
            {"name": "27", "rarity": "Common", "probability": 0.6},
            {"name": "28", "rarity": "Common", "probability": 0.6},
            {"name": "29", "rarity": "Uncommon", "probability": 0.3},
            {"name": "30", "rarity": "Uncommon", "probability": 0.3},
            {"name": "31", "rarity": "Rare", "probability": 0.1},
            {"name": "32", "rarity": "Common", "probability": 0.6},
            {"name": "33", "rarity": "Common", "probability": 0.6},
            {"name": "34", "rarity": "Uncommon", "probability": 0.3},
            {"name": "35", "rarity": "Uncommon", "probability": 0.3},
            {"name": "36", "rarity": "Rare", "probability": 0.1},
            {"name": "37", "rarity": "Common", "probability": 0.6},
            {"name": "38", "rarity": "Common", "probability": 0.6},
            {"name": "39", "rarity": "Uncommon", "probability": 0.3},
            {"name": "40", "rarity": "Uncommon", "probability": 0.3}
            ]
        self.pity_counter = 0
        self.pity_threshold = 50

    def pull(self):
        if self.pity_counter >= self.pity_threshold:
            item = self.pool[-1]["name"]
            self.pity_counter = 0
        else:
            probabilities = [item["probability"] for item in self.pool]
            item = random.choices(self.pool, weights=probabilities)[0]["name"]
            self.pity_counter += 1

        return item

game = GachaGame()
for _ in range(40):
    item = game.pull()
    print("You obtained:", item)



print("This game will be difficult at first but then possible solutions will be presented to solve the issues at hand.")
#issues at hand hinting at possible gacha related issues, i.e: debt, gambling, wasteful spending, scamming.

#pick 6 types of gacha games to work on. 3 with janky mechanics and drop rates along with low payout in currency with high bundle prices. 
#3 with a pity system and good payout in currency regardless of the payout amount.
#create percentages and pull amounts based on likelyhood of getting said top tier character.
#probablity rate of 0.2% to 100%