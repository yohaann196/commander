import random

# (item_name, drop_chance 0-1)
LOOT_TABLES = {
    "Goblin":     [("Potion", 0.4)],
    "Orc":        [("Potion", 0.3), ("Iron Sword", 0.2)],
    "Dark Knight": [("Super Potion", 0.4), ("Steel Sword", 0.25)],
}

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        actual_damage = self.damage + random.randint(-2, 2)
        print(f"{self.name} attacks {player.name} for {actual_damage} damage!")
        player.take_damage(actual_damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp}/{self.max_hp} HP.")

    def is_alive(self):
        return self.hp > 0

    def drop_loot(self, player):
        """Roll loot drops and add them to the player's inventory."""
        table = LOOT_TABLES.get(self.name, [])
        for item_name, chance in table:
            if random.random() < chance:
                player.inventory.add(item_name)
