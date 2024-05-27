from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
import random

def main():
    print("Monster Trials")
    hero_name = input("What is your name? ")
    hero = Hero(hero_name)
    beg_factory = BeginnerFactory()
    exp_factory = ExpertFactory()

    monsters = []
    for _ in range(2):
        monsters.append(beg_factory.create_random_enemy())
    monsters.append(exp_factory.create_random_enemy())

    print(f"You will face a series of 3 monsters, {hero.name}.")
    print("Defeat them all to win.")

    while hero.hp > 0 and monsters:
        print("\nChoose an enemy to attack:")
        for i, monster in enumerate(monsters):
            print(f"{i+1}. {monster}")
        choice = get_int_range("Enter choice: ", 1, len(monsters))

        print(hero)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        attack_choice = get_int_range("Enter choice: ", 1, 2)

        selected_monster = monsters[choice - 1]
        if attack_choice == 1:
            print(hero.melee_attack(selected_monster))
        else:
            print(hero.ranged_attack(selected_monster))

        if selected_monster.hp <= 0:
            print(f"You have slain the {selected_monster.name}")
            monsters.remove(selected_monster)
        else:
            print(f"{selected_monster.name} attacks!")
            monster_attack = selected_monster.melee_attack(hero)
            print(monster_attack)
            print(f"{hero.name} HP: {hero.hp}")

        if hero.hp <= 0:
            print("Game Over")
            break

    if hero.hp > 0:
        print("Congratulations! You defeated all three monsters!")

def get_int_range(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()



'''monsters = [m for m in monsters if m.hp > 0]
        if monsters:
            attacking_monster = choice(monsters)
            attack_type = choice(["basic", "special"])
            if attack_type == "basic":
                attack_message = attacking_monster.basic_attack(hero)
            else:
                attack_message = attacking_monster.special_attack(hero)
            print(attack_message)'''