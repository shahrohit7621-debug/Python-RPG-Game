import random

# Index details...
# player[0] → CHARACTER...
# player[1] → HEALTH...
# player[2] → XP...
# player[3] → LEVELS...
# player[4] → KIlls...
# player[5] → INVENTORY... 

characters = [
    ["Witch", 80, 15, 25],
    ["Mage", 90, 10, 30],
    ["Warrior", 120, 12, 20],
    ["Healer", 100, 8, 18],
    ["Brawler", 110, 14, 22]
]

rewards = ["Sword", "Shield", "Potion", "Gold", "Armor"]

# [name, health, xp, level, kills, inventory]
player = ["", 0, 0, 1, 0, []]

def choose_character():
    print("\nChoose your character:")
    for i in range(len(characters)):
        print(i + 1, ".", characters[i][0])

    choice = int(input("Enter number (1-5): "))

    if 1 <= choice <= 5:
        player[0] = characters[choice - 1][0]
        player[1] = characters[choice - 1][1]
        return characters[choice - 1][2], characters[choice - 1][3]
    else:
        print(" Invalid choice, default Warrior selected.")
        player[0] = "Warrior"
        player[1] = 120
        return 12, 20
        
# CHARACTER SELECTION 
print(" Welcome to the RPG Arena! ")
min_damage, max_damage = choose_character()

print("\n You selected:", player[0], )
print("Starting Health:", player[1])

# GAME LOOP
while True:
    print("\n--- Menu ---")
    print("1. Fight enemy")
    print("2. View status")
    print("3. View inventory")
    print("4. Exit")
    print("5. Choose Character")   

    action = input("Enter choice: ")

    if action == "1":
        enemy_health = random.randint(40, 80)
        print("\n A wild enemy appears! Enemy HP:", enemy_health)
        
        # TRACK MAX HEALTH
        max_health = [c[1] for c in characters if c[0] == player[0]][0]
        
        # FIGHT LOOP
        while enemy_health > 0 and player[1] > 0:
            print("\n--- Battle Menu ---")
            print("1. Quick Attack")
            print("2. Heavy Attack")
            print("3. Heal")
            print("4. Go Back to Menu")   

            move = input("Choose your move: ")

            if move == "1":
                dmg = random.randint(min_damage, max_damage)
                print(" You used Quick Attack! Damage:", dmg)
                enemy_health -= dmg

            elif move == "2":
                dmg = random.randint(min_damage + 5, max_damage + 10)
                print(" You used Heavy Attack! Damage:", dmg)
                enemy_health -= dmg
                
                counter = random.randint(10, 20)
                player[1] -= counter
                print(" Enemy counterattacked for", counter, "damage!")

            elif move == "3":
                heal = random.randint(10, 20)
                player[1] += heal
                if player[1] > max_health:
                    player[1] = max_health
                print(" You healed yourself for", heal, "HP!")

            elif move == "4":
                print(" You retreated back to the Menu!")
                break   

            else:
                print(" Invalid move, you lost your turn!")
            
             # ENEMY ATTACK
            if move != "4" and enemy_health > 0:   
                enemy_attack = random.randint(5, 15)
                player[1] -= enemy_attack
                print(" Enemy attacks you for", enemy_attack, "damage!")
            # SHOW STATUS
            if move != "4":
                print(" Your HP:", player[1], "| Enemy HP:", enemy_health)
        
        # AFTER FIGHT 
        if move == "4":   
            continue

        if player[1] > 0:
            print("\n Enemy defeated!")
            player[4] += 1       
            player[2] += 5       
            
            # HEALTH RECOVER +5 AFTER EVERY GAME...
            player[1] += 5
            if player[1] > max_health:
                player[1] = max_health
            print(f" You recovered 5 HP! Current Health: {player[1]}")
            # REWARD AFTER FIGHT
            reward = random.choice(rewards)
            player[5].append(reward)
            print(f" You received a guaranteed reward: {reward}")
            
            choice = input(" Do you want to exit? (y/n): ")
            if choice.lower() == "y":
                print(" Thanks for playing!")
                break
                
        else:
            print("\n You were defeated in battle!")
            choice = input(" Do you want to play again? (y/n): ")
            if choice.lower() == "y":
                player = ["", 0, 0, 1, 0, []]   # RESET PLAYER...
                min_damage, max_damage = choose_character()  # CHOSSE NEW CHARACTER...
                print("\n You are reset and back to Menu.")
                continue
            else:
                print(" Thanks for playing!")
                break
        # LEVEL UP CHECK       
        if player[2] >= 10:
            player[3] += 1
            player[2] = 0
            print(" You leveled up! Now Level", player[3])
            
            level_reward = random.choice(rewards)
            player[5].append(level_reward)
            print(" You received a special reward for leveling up:", level_reward)

    elif action == "2":
        print("\n--- Status ---")
        print("Character:", player[0])
        print("Health:", player[1])
        print("Level:", player[3])
        print("XP:", player[2])
        print("Kills:", player[4])

    elif action == "3":
        print("\n--- Inventory ---")
        if len(player[5]) == 0:
            print("Empty")
        else:
            for item in player[5]:
                print("-", item)

    elif action == "4":
        print(" Thanks for playing!")
        break

    elif action == "5": 
        min_damage, max_damage = choose_character()
        player[2] = 0
        player[3] = 1
        player[4] = 0
        player[5] = []
        print("\n You changed to:", player[0],)
        print("Health reset to:", player[1])

    else:
        print(" Invalid choice, try again.")