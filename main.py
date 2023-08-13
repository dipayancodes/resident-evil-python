import random

# Define the game map
game_map = [
    ["Room 1", "Corridor", "Room 2"],
    ["Corridor", "Room 3", "Corridor"],
    ["Room 4", "Corridor", "Room 5"]
]

# Define characters and their attributes
characters = {
    "Leon": {"health": 100, "damage": 30},
    "Ada Wong": {"health": 80, "damage": 40},
    "Chris": {"health": 120, "damage": 25}
}

# Define weapons and their damage
weapons = {
    "Knife": 20,
    "Handgun": 40,
    "Shotgun": 60
}

# Define items and their effects
items = {
    "Herb": {"health": 30},
    "First Aid Spray": {"health": 50}
}

# Define enemies and their health
enemies = {
    "Zombie": 50,
    "Licker": 75,
    "Hunter": 100
}

# Define boss types and their health
bosses = {
    "Tyrant": 150,
    "Nemesis": 200
}

# Define Duke's items and prices
duke_items = {
    "Handgun": 100,
    "Shotgun": 200,
    "Ammo Pack": 20
}

# Player's starting position
player_position = [0, 0]

# Player's selected character (default: Leon)
selected_character = "Leon"

# Player's equipped weapon (default: Knife)
equipped_weapon = "Knife"

# Player's health ( default: 100)
player_health = 100

# Player's inventory
inventory = []

# Player's currency
player_currency = 150

# Main game loop
while True:
    current_room = game_map[player_position[0]][player_position[1]]
    print("You are in", current_room)

    action = input("What will you do? (move/interact/equip/select/buy/quit): ").lower()

    if action == "quit":
        print("Thanks for playing!")
        break
    elif action == "move":
        direction = input("Where do you want to move? (up/down/left/right): ").lower()

        if direction == "up" and player_position[0] > 0:
            player_position[0] -= 1
        elif direction == "down" and player_position[0] < len(game_map) - 1:
            player_position[0] += 1
        elif direction == "left" and player_position[1] > 0:
            player_position[1] -= 1
        elif direction == "right" and player_position[1] < len(game_map[0]) - 1:
            player_position[1] += 1
        else:
            print("You can't move in that direction.")

    elif action == "interact":
        if current_room == "Room 3":
            print("You encounter a boss!")
            boss_type = random.choice(list(bosses.keys()))
            boss_health = bosses[boss_type]
            print(f"A {boss_type} attacks you!")
            while boss_health > 0:
                player_attack = random.randint(10, 40)
                boss_health -= player_attack
                print(f"You attack the {boss_type} for {player_attack} damage.")
                print(f"{boss_type} health:", boss_health)
                if boss_health > 0:
                    boss_attack = random.randint(20, 50)
                    print(f"The {boss_type} attacks you for {boss_attack} damage.")
                    player_health -= boss_attack
                    print("Your health:", player_health)
                    if player_health <= 0:
                        print("You have been defeated.")
                        break
                else:
                    print(f"You defeated the {boss_type} and earned 100 currency.")
                    player_currency += 100
                    print(f"Current currency: {player_currency}")
                    break
        else:
            # Simulated enemy encounter
            if random.random() < 0.4:
                enemy_type = random.choice(list(enemies.keys()))
                enemy_health = enemies[enemy_type]
                print(f"An {enemy_type} attacks you!")
                while enemy_health > 0:
                    player_attack = random.randint(10, 40)
                    enemy_health -= player_attack
                    print(f"You attack the {enemy_type} for {player_attack} damage.")
                    print(f"{enemy_type} health:", enemy_health)
                    if enemy_health > 0:
                        player_health -= random.randint(10, 30)
                        print(f"The {enemy_type} attacks you for {player_attack} damage.")
                        print("Your health:", player_health)
                        if player_health <= 0:
                            print("You have been defeated.")
                            break
                    else:
                        print(f"You defeated the {enemy_type} and earned 10 currency.")
                        player_currency += 10
                        print(f"Current currency: {player_currency}")
                        break
            else:
                print("You didn't find anything to interact with.")

    elif action == "equip":
        if inventory:
            print("Choose a weapon to equip:")
            for index, item in enumerate(inventory):
                print(f"{index + 1}. {item}")
            weapon_choice = int(input("Enter the number of the weapon: ")) - 1

            if 0 <= weapon_choice < len(inventory):
                equipped_weapon = inventory[weapon_choice]
                print(f"You have equipped {equipped_weapon}.")
            else:
                print("Invalid choice.")
        else:
            print("You don't have any weapons in your inventory.")

    elif action == "select":
        print("Choose a character:")
        for character in characters:
            print(character)
        character_choice = input("Enter the name of the character (or press Enter to keep default): ").strip()

        if character_choice == "":
            print("Using default character: Leon")
        elif character_choice in characters:
            selected_character = character_choice
            print(f"You have selected {selected_character}.")
        else:
            print("Invalid choice. Using default character: Leon.")

    elif action == "buy":
        print("Welcome to Duke's shop!")
        print("Available items:")
        for item, price in duke_items.items():
            print(f"{item} - {price} currency")

        item_choice = input("Enter the name of the item you want to buy: ")
        if item_choice in duke_items:
            item_price = duke_items[item_choice]
            if player_currency >= item_price:
                inventory.append(item_choice)
                player_currency -= item_price
                print(f"You bought {item_choice}.")
                print(f"Remaining currency: {player_currency}")
            else:
                print("You don't have enough currency.")
        else:
            print("Invalid item choice.")

    else:
        print("Invalid action. Choose 'move', 'interact', 'equip', 'select', 'buy', or 'quit'.")
