import random

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
