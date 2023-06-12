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
        self.pity_threshold = 5
        self.currency_balance = 0
        self.currency_price = 10
        self.bank_balance = 500

    def pull(self):
        if self.pity_counter >= self.pity_threshold:
            item = self.pool[-1]["name"]
            self.pity_counter = 0
        else:
            probabilities = [item["probability"] for item in self.pool]
            item = random.choices(self.pool, weights=probabilities)[0]["name"]
            self.pity_counter += 1

        self.currency_balance += 1  # Earn pity point with each pull
        return item["name"], item["rarity"]

    def purchase_currency(self, amount):
        cost = amount * self.currency_price
        self.bank_balance -= cost
        self.currency_balance += amount
        print(f"You purchased {amount} coins for a total cost of {cost}.")

    def play_game(self):
        print("Welcome to the GACHA SIMULATOR where you can experience the chance based system firsthand.")
        while True:
            choice = input("Enter '1x' for a single pull, '10x' for a 10 pull, 'buy' to purchase coins for pulls, 'bal' to check bank balance, or 'q' to quit: ")

            if choice == '1x':
                if self.currency_balance > 0:
                    item_name, item_rarity = self.pull()
                    print(f"You obtained: {item_name} (Rarity: {item_rarity})")
                    self.currency_balance -= 1
                else:
                    print("Insufficient coins. Purchase more to continue.")
            elif choice == '10x':
                if self.currency_balance >= 10:
                    self.ten_pull()
                    self.currency_balance -= 10
                else:
                    print("Insufficient coins. Purchase more to continue.")
            elif choice.lower() == 'buy':
                amount = int(input("Enter the amount of coins to purchase: "))
                self.purchase_currency(amount)
            elif choice.lower() == 'bal':
                print("Bank balance:", self.bank_balance)
            elif choice.lower() == 'q':
                print("Thanks for trying it out!")
                break
            else:
                print("Invalid choice. Please try again.")

    def ten_pull(self):
        print("Performing a 10 pull...")
        for _ in range(10):
            item_name, item_rarity = self.pull()
            print(f"You obtained: {item_name} (Rarity: {item_rarity})")
        print("10 pull complete!")

game = GachaGame()
game.play_game()
