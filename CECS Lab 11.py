from check_input import get_int_range
from dwarf import Dwarf
from elf import Elf
from halfling import Halfling
from archery import Archery
from fighting import Fighting
from fire import Fire
from healing import Healing

def main():
    print("Character Maker!")
    print("Choose your character:")
    print("1. Dwarf")
    print("2. Elf")
    print("3. Halfling")
    choice = get_int_range("Enter choice: ", 1, 3)
    
    if choice == 1:
        character = Dwarf(input("What is your character's name? "))
    elif choice == 2:
        character = Elf(input("What is your character's name? "))
    else:
        character = Halfling(input("What is your character's name? "))

    print(character)

    print("You have 5 points to spend:")
    for _ in range(5):
        print("Add an ability:")
        print("1. Archery")
        print("2. Fighting")
        print("3. Fire Magic")
        print("4. Healing")
        ability = get_int_range("Enter ability: ", 1, 4)

        if ability == 1:
            character = Archery(character)
        elif ability == 2:
            character = Fighting(character)
        elif ability == 3:
            character = Fire(character)
        else:
            character = Healing(character)

        print(character)

    if character.constitution() <= 0 or character.strength() <= 0 or character.wisdom() <= 0:
        print("You have failed at making a character.")
    else:
        print("Congratulations! You have created your character.")

if __name__ == "__main__":
    main()
