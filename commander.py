from game.player import Player
from game.enemy import Enemy
from game.battle import battle
import random

def main():
    print("Welcome to Commander: the videogame that runs in your terminal!\n")
    name = input("Enter your name, Commander: ")
    player = Player(name)

    enemies = [
        Enemy("Goblin", 30, 5),
        Enemy("Orc", 50, 8),
        Enemy("Dark Knight", 70, 12)
    ]

    while player.is_alive():
        enemy = random.choice(enemies)
        battle(player, enemy)

        if not player.is_alive():
            break

        print("\nDo you want to continue exploring? (y/n)")
        cont = input("> ").lower()
        if cont != "y":
            print(f"Good job, Commander {player.name}! You finished with {player.hp}/{player.max_hp} HP and {player.exp} EXP.")
            print("Final inventory:")
            player.inventory.show()
            break

if __name__ == "__main__":
    main()
