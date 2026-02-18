import random

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.level = 1
        self.exp = 0
        self.inventory = {"Potion": 2}
        self.weapon = {"name": "Fist", "damage": 5}

    def attack(self, enemy):
        damage = self.weapon["damage"] + random.randint(-2, 2)
        print(f"{self.name} attacks {enemy.name} with {self.weapon['name']} for {damage} damage!")
        enemy.take_damage(damage)

    def heal(self):
        if self.inventory.get("Potion", 0) > 0:
            heal_amount = random.randint(15, 25)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.inventory["Potion"] -= 1
            print(f"{self.name} uses a Potion and heals {heal_amount} HP! ({self.hp}/{self.max_hp})")
        else:
            print("No potions left!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp}/{self.max_hp} HP.")

    def is_alive(self):
        return self.hp > 0
