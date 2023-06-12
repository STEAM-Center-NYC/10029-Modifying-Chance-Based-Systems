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
            {"name": "13", "rarity": "Uncommon", "probability": 0.6},
            {"name": "14", "rarity": "Uncommon", "probability": 0.6},
            {"name": "15", "rarity": "Uncommon", "probability": 0.6},
            {"name": "16", "rarity": "Uncommon", "probability": 0.6},
            {"name": "17", "rarity": "Uncommon", "probability": 0.6},
            {"name": "18", "rarity": "Uncommon", "probability": 0.6},
            {"name": "19", "rarity": "Uncommon", "probability": 0.6},
            {"name": "20", "rarity": "Uncommon", "probability": 0.6},
            {"name": "22", "rarity": "Uncommon", "probability": 0.6},
            {"name": "23", "rarity": "Uncommon", "probability": 0.6},
            {"name": "24", "rarity": "Uncommon", "probability": 0.6},
            {"name": "25", "rarity": "Uncommon", "probability": 0.6},
            {"name": "26", "rarity": "Rare", "probability": 0.4},
            {"name": "27", "rarity": "Rare", "probability": 0.4},
            {"name": "28", "rarity": "Rare", "probability": 0.4},
            {"name": "29", "rarity": "Rare", "probability": 0.4},
            {"name": "30", "rarity": "Rare", "probability": 0.4},
            {"name": "31", "rarity": "Rare", "probability": 0.4},
            {"name": "32", "rarity": "Rare", "probability": 0.4},
            {"name": "33", "rarity": "Rare", "probability": 0.4},
            {"name": "34", "rarity": "Rare", "probability": 0.4},
            {"name": "35", "rarity": "Rare", "probability": 0.4},
            {"name": "36", "rarity": "Rare", "probability": 0.4},
            {"name": "37", "rarity": "Rare", "probability": 0.4},
            {"name": "38", "rarity": "Rare", "probability": 0.4},
            {"name": "39", "rarity": "Rare", "probability": 0.4},
            {"name": "40", "rarity": "Rare", "probability": 0.4},
            {"name": "41", "rarity": "Exotic", "probability": 0.2},
            {"name": "42", "rarity": "Exotic", "probability": 0.2},
            {"name": "43", "rarity": "Exotic", "probability": 0.2},
            {"name": "44", "rarity": "Exotic", "probability": 0.2},
            {"name": "45", "rarity": "Exotic", "probability": 0.2},
            {"name": "46", "rarity": "Exotic", "probability": 0.2},
            {"name": "47", "rarity": "Exotic", "probability": 0.2},
            {"name": "48", "rarity": "Exotic", "probability": 0.2},
            {"name": "49", "rarity": "Exotic", "probability": 0.2},
            {"name": "50", "rarity": "Exotic", "probability": 0.2},
            {"name": "51", "rarity": "Exotic", "probability": 0.2},
            {"name": "52", "rarity": "Exotic", "probability": 0.2},
            {"name": "53", "rarity": "Exotic", "probability": 0.2},
            {"name": "54", "rarity": "Exotic", "probability": 0.2},
            {"name": "55", "rarity": "Legendary", "probability": 0.1},
            {"name": "56", "rarity": "Legendary", "probability": 0.1},
            {"name": "57", "rarity": "Legendary", "probability": 0.1},
            {"name": "58", "rarity": "Legendary", "probability": 0.1},
            {"name": "59", "rarity": "Legendary", "probability": 0.1},
            {"name": "60", "rarity": "Legendary", "probability": 0.1},
            {"name": "61", "rarity": "Legendary", "probability": 0.1},
            {"name": "62", "rarity": "Legendary", "probability": 0.1},
            {"name": "63", "rarity": "Legendary", "probability": 0.1},
            {"name": "64", "rarity": "Legendary", "probability": 0.1},
            {"name": "65", "rarity": "Legendary", "probability": 0.1},
            {"name": "66", "rarity": "Legendary", "probability": 0.1},
            {"name": "67", "rarity": "Legendary", "probability": 0.1}
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