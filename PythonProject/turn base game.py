import random
inventory = {"Small potion": 0, "Big potion": 0, "Gold": 0}
hidden_goblin_view = False

def show_inventory():
    print("\n--- INVENTORY ---")
    for item, amount in inventory.items():
        print(f"{item}: {amount}")


def goblin_drop():
    drop_roll = random.randint(1, 100)
    if drop_roll <= 45:
        print("The goblin dropped nothing.")
    elif drop_roll <= 70:
        print("The goblin dropped 10 gold.")
        inventory["Gold"] += 10
    elif drop_roll <= 85:
        print("The goblin dropped small potion.")
        inventory["Small potion"] += 1
    elif drop_roll <= 95 and hidden_goblin_view:
        print("The goblin dropped 50 gold.")
        inventory["Gold"] += 50

    elif drop_roll <= 100 and hidden_goblin_view:
        print("The goblin dropped 1 big potion.")
        inventory["Big potion"] += 1
    else:
        print("You need to buy goblin view to get better loot")
    show_inventory()


def battle_game(player_health, player_defense, enemy_health, enemy_damage_range, crit_chance, dodge_chance, regen):
    print(f"A wild {enemy_type} appears!")

    while player_health > 0 and enemy_health > 0:
        print("\nYour Health:", player_health)
        print(enemy_type, "Health:", enemy_health)
        choice = input("1) Attack\n2) Defend\nChoose: ")
        defending = False

        if choice == "1":
            damage = random.randint(5, 20)

            if random.random() < crit_chance:
                damage *= 1.2
                print("\nYou landed a CRITICAL HIT!")
            enemy_health -= damage
            print("\nYou dealt", damage, "damage!")


        elif choice == "2":
            defending = True
            print("\nYou brace yourself and prepare to defend!")
        else:
            print("You missed your turn!")
        if regen > 0:
            player_health += regen
            print("You regenerated", regen, "health!")
        if enemy_health > 0:
            enemy_damage = random.randint(enemy_damage_range[0], enemy_damage_range[1])
            if random.random() < .10:
                enemy_damage *= 1.2
                print("\nENEMY LAND A CRITICAL HIT!")
            if defending:
                enemy_damage = enemy_damage * (1 - player_defense)
            if random.random() < dodge_chance:
                enemy_damage = 0
                print("You dodged the attack!")
            player_health -= int(enemy_damage)
            print("\nThe enemy dealt", round(enemy_damage, 2), "damage!")
    if player_health <= 0:
            print("\nYou lost the battle.")
            return False
    else:
            print("\nYou won the battle!\n")
            return True




'''if win == battle_game(player_health, player_defense, enemy_health, enemy_damage_range, crit_chance, dodge_chance, regen):
    

    
    drop_roll = random.randint(1, 100)
    if enemy_type == "Goblin":
        if drop_roll <= 45:
            #drop nothing
        elif drop_roll <= 70:

        elif drop_roll <= 85:

        elif drop_roll <= 95:

        elif drop_roll <= 100:
    elif enemy_type == "Orc":
        if drop_roll <= 45:
        # drop nothing
        elif drop_roll <= 70:

        elif drop_roll <= 85:

        elif drop_roll <= 95:

        elif drop_roll <= 100:

    elif enemy_type == "Dragon":
        if drop_roll <= 45:
        # drop nothing
        elif drop_roll <= 70:

        elif drop_roll <= 85:

        elif drop_roll <= 95:

        elif drop_roll <= 100:
I will use this later in the game when i have made a shop and inventory and coin counter
'''


while True:
    print("Welcome!")
    print("Choose your character class:")
    print("1) Warrior (high health, medium defense)")
    print("2) Mage (lower health, balanced)")
    print("3) Rogue (balanced, higher defense)")
    print("4) Rizzer (unknown health, unknown defense)")

    char_choice = input("Choose (1/2/3/4): ")

    if char_choice == "1":
        base_health = 120
        base_defense = 0.3
        base_crit = 0.15
        base_dodge = 0.05
        base_regen = 5
    elif char_choice == "2":
        base_health = 90
        base_defense = 0.2
        base_crit = 0.16
        base_dodge = 0.05
        base_regen = 0
    elif char_choice == "3":
        base_health = 100
        base_defense = 0.4
        base_crit = 0.20
        base_dodge = 0.1
        base_regen = 0
    elif char_choice == "4":
        base_health = 10
        base_defense = 1.2
        base_crit = 0.5
        base_dodge = 0.5
        base_regen = 15
    else:
        print("Invalid choice, defaulting to Warrior.")
        base_health = 120
        base_defense = 0.3

    enemy_type = random.choice(["Goblin", "Orc", "Dragon"])
    if enemy_type == "Goblin":
        enemy_health = 70
        enemy_damage = (5, 15)
    elif enemy_type == "Orc":
        enemy_health = 100
        enemy_damage = (7, 20)
    elif enemy_type == "Dragon":
        enemy_health = 150
        enemy_damage = (15, 40)

    difficulty = input("Choose your difficulty(easy, normal, hard, impossible): ").lower()

    if difficulty == "easy":
        win = battle_game(base_health + 20, base_defense + 0.3, enemy_health - 10, enemy_damage, base_crit, base_dodge, base_regen)
    elif difficulty == "normal":
        win = battle_game(base_health + 15, base_defense + 0.2, enemy_health, enemy_damage, base_crit, base_dodge, base_regen)
    elif difficulty == "hard":
        win = battle_game(base_health + 10, base_defense + 0.1, enemy_health + 10, enemy_damage, base_crit, base_dodge, base_regen)
    elif difficulty == "impossible":
        win = battle_game(base_health + 5, base_defense + 0.1, enemy_health + 15, (enemy_damage[0], enemy_damage[1] + 5), base_crit, base_dodge, base_regen)
    else:
        print("Invalid difficulty.")
        continue
    if win:
        if enemy_type == "Goblin":
            goblin_drop()
    shop = input("Would you like to visit the shop? (y/n): ").lower()
    if shop == "y":
        goblin_view = input("Would you like to view the hidden goblin drop for 20 gold? (y/n): ").lower()
        if goblin_view == "y" and inventory["Gold"] >= 20:
            inventory["Gold"] -= 20
            hidden_goblin_view = True
            print("You have bought goblin view!")
        else:
            print("You have not bought goblin view!")

    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break