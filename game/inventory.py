import random

# Base weapon damage for a bare-handed player (must match player.py)
BASE_WEAPON_DAMAGE = 5

# All usable / equippable items in the game
ITEMS = {
    "Potion": {
        "type": "consumable",
        "description": "Restores 15-25 HP",
        "heal_min": 15,
        "heal_max": 25,
    },
    "Super Potion": {
        "type": "consumable",
        "description": "Restores 35-50 HP",
        "heal_min": 35,
        "heal_max": 50,
    },
    "Iron Sword": {
        "type": "weapon",
        "description": "+5 Attack",
        "damage_bonus": 5,
    },
    "Steel Sword": {
        "type": "weapon",
        "description": "+10 Attack",
        "damage_bonus": 10,
    },
}


class Inventory:
    """Manages the player's carried items."""

    def __init__(self, starting_items=None):
        # {item_name: quantity}
        self.items = {}
        if starting_items:
            for item, qty in starting_items.items():
                self.add(item, qty)

    def add(self, item_name, quantity=1):
        if item_name not in ITEMS:
            return
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        print(f"  [Inventory] Obtained {quantity}x {item_name}!")

    def remove(self, item_name, quantity=1):
        if self.items.get(item_name, 0) < quantity:
            return False
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]
        return True

    def has(self, item_name):
        return self.items.get(item_name, 0) > 0

    def show(self):
        if not self.items:
            print("  (Inventory is empty)")
            return
        print("  --- Inventory ---")
        for idx, (name, qty) in enumerate(self.items.items(), start=1):
            desc = ITEMS[name]["description"]
            print(f"  {idx}. {name} x{qty}  [{desc}]")
        print("  -----------------")

    def use_item(self, item_name, player):
        """Use or equip *item_name*.  Returns True if something happened."""
        if not self.has(item_name):
            print(f"You don't have any {item_name}.")
            return False

        data = ITEMS.get(item_name, {})
        itype = data.get("type")

        if itype == "consumable":
            if player.hp >= player.max_hp:
                print(f"{player.name} is already at full HP!")
                return False
            amount = random.randint(
                data.get("heal_min", 15),
                data.get("heal_max", 25),
            )
            healed = min(amount, player.max_hp - player.hp)
            player.hp += healed
            self.remove(item_name)
            print(f"{player.name} uses {item_name} and restores {healed} HP! ({player.hp}/{player.max_hp})")
            return True

        if itype == "weapon":
            new_damage = BASE_WEAPON_DAMAGE + data.get("damage_bonus", 0)
            if new_damage > player.weapon.get("damage", 0):
                player.weapon = {"name": item_name, "damage": new_damage}
                self.remove(item_name)
                print(f"{player.name} equips {item_name}! Attack is now {player.weapon['damage']}.")
                return True
            else:
                print(f"{item_name} is not better than your current weapon.")
                return False

        print(f"Cannot use {item_name}.")
        return False

    def interactive_use(self, player):
        """Show inventory and prompt the player to pick an item to use."""
        if not self.items:
            print("Your inventory is empty!")
            return False
        self.show()
        names = list(self.items.keys())
        choice = input("Use which item? (name or number, or 'back'): ").strip()
        if choice.lower() == "back":
            return False
        # Accept number or name
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(names):
                item_name = names[idx]
            else:
                print("Invalid selection.")
                return False
        else:
            item_name = choice
        return self.use_item(item_name, player)
