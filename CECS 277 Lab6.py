from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from check_input import get_int_range
from random import choice

def main():
    p = input("What is your name challenger?\n")
    print("Welcome to dragon training,", p)
    print("You must defeat 3 dragons.\n")
    hero = Hero("Hero", 50)
    dragons = [
        Dragon("Deadly Nadder", 10),
        FireDragon("Gronckle", 15, 3),
        FlyingDragon("Timberjack", 20, 5)]

    while dragons:
        print(p,":", hero.hp,"/ 50")
        for i, dragon in enumerate(dragons):
            print(f"{i + 1}. {dragon}")

        dragon_choice = get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        print("Choose an attack:")
        print("1. Sword Attack")
        print("2. Arrow Attack")
        attack_choice = get_int_range("Enter your choice: ", 1, 2)
        dragon = dragons[dragon_choice - 1]
        if attack_choice == 1:
            message = hero.sword_attack(dragon)
        else:
            message = hero.arrow_attack(dragon)
        print(message)

        if dragon.hp <= 0:
            print(f"{dragon.name} has been defeated!")
            dragons.remove(dragon)
            continue

        _dragons = [d for d in dragons if d.hp > 0]
        if _dragons:
            attacking_dragon = choice(_dragons)
            attack_type = choice(["basic", "special"])
            if attack_type == "basic":
                attack_message = attacking_dragon.basic_attack(hero)
            else:
                attack_message = attacking_dragon.special_attack(hero)
            print(attack_message)

        if hero.hp <= 0:
            print("You have been knocked out!")
            break

    if not dragons:
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials.!")

if __name__ == "__main__":
    main()

