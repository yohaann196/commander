import random
from game.inventory import Inventory, BASE_WEAPON_DAMAGE

EXP_PER_LEVEL = 20

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.level = 1
        self.exp = 0
        self.exp_to_next = EXP_PER_LEVEL
        self.inventory = Inventory({"Potion": 2})
        self.weapon = {"name": "Fist", "damage": BASE_WEAPON_DAMAGE}

    def attack(self, enemy):
        damage = self.weapon["damage"] + random.randint(-2, 2)
        print(f"{self.name} attacks {enemy.name} with {self.weapon['name']} for {damage} damage!")
        enemy.take_damage(damage)

    def heal(self):
        """Quick-use the first available potion from inventory."""
        for potion in ("Super Potion", "Potion"):
            if self.inventory.has(potion):
                self.inventory.use_item(potion, self)
                return
        print("No potions left!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp}/{self.max_hp} HP.")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"You gained {amount} EXP! ({self.exp}/{self.exp_to_next})")
        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self._level_up()

    def _level_up(self):
        self.level += 1
        hp_gain = 20
        dmg_gain = 3
        self.max_hp += hp_gain
        self.hp = self.max_hp  # full heal on level up
        self.weapon["damage"] += dmg_gain
        self.exp_to_next = EXP_PER_LEVEL * self.level
        print(f"\n*** LEVEL UP! You are now Level {self.level}! ***")
        print(f"  Max HP +{hp_gain} -> {self.max_hp}")
        print(f"  Attack +{dmg_gain} -> {self.weapon['damage']}")
        print(f"  HP fully restored!\n")

    def is_alive(self):
        return self.hp > 0
