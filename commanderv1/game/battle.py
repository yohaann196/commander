import random

def battle(player, enemy):
    print(f"\nA wild {enemy.name} appears!\n")

    while player.is_alive() and enemy.is_alive():
        print("\nYour turn:")
        print("1. Attack")
        print("2. Heal")
        action = input("> ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.heal()
        else:
            print("Invalid action! You lose your turn.")

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print(f"\n{player.name} defeated {enemy.name}!")
        gained = random.randint(5, 15)
        player.gain_exp(gained)
    else:
        print(f"\n{player.name} was defeated by {enemy.name}... Game Over.")
