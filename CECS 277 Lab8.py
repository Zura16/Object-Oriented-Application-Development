import random
from check_input import get_int_range
from basic_door import BasicDoor
from locked_door import LockedDoor
from deadbolt_door import DeadboltDoor
from combo_door import ComboDoor
from code_door import CodeDoor

def open_door(door):
    print(door.examine_door())
    print(door.menu_options())
    option = get_int_range("Enter your choice: ", 1, door.get_menu_max())
    result = door.attempt(option)
    print(result)
    if door.is_unlocked():
        print(door.success())
    else:
        print(door.clue())
        open_door(door)

def main():
    doors = [BasicDoor(), LockedDoor(), DeadboltDoor(), ComboDoor(), CodeDoor()]
    for i in range(2):
        print(f"Door {i+1}:")
        open_door(random.choice(doors))
    print("Congratulations! You've successfully opened all the doors!")

if __name__ == "__main__":
    main()
