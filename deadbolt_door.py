import random
from door import Door

class DeadboltDoor(Door):
    """A door with two deadbolts that need to be unlocked."""

    def __init__(self):
        self.bolt1 = random.choice([True, False])
        self.bolt2 = random.choice([True, False])
        self.unlocked = False

    def examine_door(self):
        return "A door with two deadbolts. Both need to be unlocked to open the door."

    def menu_options(self):
        return "1. Toggle bolt 1\n2. Toggle bolt 2"

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        if option == 1:
            self.bolt1 = not self.bolt1
            print("You toggle the first bolt.")
        elif option == 2:
            self.bolt2 = not self.bolt2
            print("You toggle the second bolt.")

        if not self.bolt1 and not self.bolt2:
            self.unlocked = True
            return "You unlocked both bolts!"
        else:
            return "You jiggle the door...it seems like one of the bolts is unlocked."

    def is_unlocked(self):
        return self.unlocked

    def clue(self):
        return "...it seems like its completely locked."

    def success(self):
        return "Congratulations! You've successfully opened the door!"
