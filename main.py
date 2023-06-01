print("Welcome to the GACHA SIMULATOR where you can experience the chance based system firsthand.")
#not called Gacha Simulator, temporary placeholder until better name is found.

import random

class GachaGame:
    def __init__(self):
        self.pool = [
            {"name": "1", "rarity": "Common", "probability": 1.0},
            {"name": "2", "rarity": "Common", "probability": 1.0},
            {"name": "3", "rarity": "Common", "probability": 1.0},
            {"name": "4", "rarity": "Common", "probability": 1.0},
            {"name": "5", "rarity": "Common", "probability": 1.0},
            {"name": "6", "rarity": "Common", "probability": 1.0},
            {"name": "7", "rarity": "Common", "probability": 1.0},
            {"name": "8", "rarity": "Common", "probability": 1.0},
            {"name": "9", "rarity": "Common", "probability": 1.0},
            {"name": "10", "rarity": "Common", "probability": 1.0},
            {"name": "11", "rarity": "Common", "probability": 1.0},
            {"name": "12", "rarity": "Common", "probability": 1.0},
            {"name": "13", "rarity": "common", "probability": 1.0},
            {"name": "14", "rarity": "common", "probability": 1.0},
            {"name": "15", "rarity": "common", "probability": 1.0},
            {"name": "16", "rarity": "common", "probability": 1.0},
            {"name": "17", "rarity": "common", "probability": 1.0},
            {"name": "18", "rarity": "common", "probability": 1.0},
            {"name": "19", "rarity": "common", "probability": 1.0},
            {"name": "20", "rarity": "common", "probability": 1.0},
            {"name": "22", "rarity": "Uncommon", "probability": 0.6},
            {"name": "23", "rarity": "Uncommon", "probability": 0.6},
            {"name": "24", "rarity": "Uncommon", "probability": 0.6},
            {"name": "25", "rarity": "Uncommon", "probability": 0.6},
            {"name": "26", "rarity": "Uncommon", "probability": 0.6},
            {"name": "27", "rarity": "Uncommon", "probability": 0.6},
            {"name": "28", "rarity": "Uncommon", "probability": 0.6},
            {"name": "29", "rarity": "Uncommon", "probability": 0.6},
            {"name": "30", "rarity": "Uncommon", "probability": 0.6},
            {"name": "31", "rarity": "Uncommon", "probability": 0.6},
            {"name": "32", "rarity": "Uncommon", "probability": 0.6},
            {"name": "33", "rarity": "Uncommon", "probability": 0.6},
            {"name": "34", "rarity": "Uncommon", "probability": 0.6},
            {"name": "35", "rarity": "Uncommon", "probability": 0.6},
            {"name": "36", "rarity": "Uncommon", "probability": 0.6},
            {"name": "37", "rarity": "Uncommon", "probability": 0.6},
            {"name": "38", "rarity": "Uncommon", "probability": 0.6},
            {"name": "39", "rarity": "Uncommon", "probability": 0.6},
            {"name": "40", "rarity": "Uncommon", "probability": 0.6},
            {"name": "41", "rarity": "Rare", "probability": 0.4},
            {"name": "42", "rarity": "Rare", "probability": 0.4},
            {"name": "43", "rarity": "Rare", "probability": 0.4},
            {"name": "44", "rarity": "Rare", "probability": 0.4},
            {"name": "45", "rarity": "Rare", "probability": 0.4},
            {"name": "46", "rarity": "Rare", "probability": 0.4},
            {"name": "47", "rarity": "Rare", "probability": 0.4},
            {"name": "48", "rarity": "Rare", "probability": 0.4},
            {"name": "49", "rarity": "Rare", "probability": 0.4},
            {"name": "50", "rarity": "Rare", "probability": 0.4},
            {"name": "51", "rarity": "Rare", "probability": 0.4},
            {"name": "52", "rarity": "Rare", "probability": 0.4},
            {"name": "53", "rarity": "Rare", "probability": 0.4},
            {"name": "54", "rarity": "Rare", "probability": 0.4},
            {"name": "55", "rarity": "Rare", "probability": 0.4},
            {"name": "56", "rarity": "Rare", "probability": 0.4},
            {"name": "57", "rarity": "Rare", "probability": 0.4},
            {"name": "58", "rarity": "Rare", "probability": 0.4},
            {"name": "59", "rarity": "Rare", "probability": 0.4},
            {"name": "60", "rarity": "Rare", "probability": 0.4},
            {"name": "61", "rarity": "Exotic", "probability": 0.2},
            {"name": "62", "rarity": "Exotic", "probability": 0.2},
            {"name": "63", "rarity": "Exotic", "probability": 0.2},
            {"name": "64", "rarity": "Exotic", "probability": 0.2},
            {"name": "65", "rarity": "Exotic", "probability": 0.2},
            {"name": "66", "rarity": "Exotic", "probability": 0.2},
            {"name": "67", "rarity": "Exotic", "probability": 0.2},
            {"name": "68", "rarity": "Exotic", "probability": 0.2},            
            {"name": "69", "rarity": "Exotic", "probability": 0.2},
            {"name": "70", "rarity": "Exotic", "probability": 0.2},
            {"name": "71", "rarity": "Legendary", "probability": 0.1},            
            {"name": "72", "rarity": "Legendary", "probability": 0.1},            
            {"name": "73", "rarity": "Legendary", "probability": 0.1},            
            {"name": "74", "rarity": "Legendary", "probability": 0.1},            
            {"name": "75", "rarity": "Legendary", "probability": 0.1},           
            {"name": "76", "rarity": "Legendary", "probability": 0.1},
            {"name": "77", "rarity": "Legendary", "probability": 0.1},
            {"name": "78", "rarity": "Legendary", "probability": 0.1},
            {"name": "79", "rarity": "Legendary", "probability": 0.1},
            {"name": "80", "rarity": "Legendary", "probability": 0.1},
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
