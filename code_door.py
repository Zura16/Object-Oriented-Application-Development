import random
from door import Door

class CodeDoor(Door):
    def __init__(self):
        self.code = [random.choice(['X', 'O']) for _ in range(3)]
        self.unlocked = False

    def examine_door(self):
        return "A door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’."

    def menu_options(self):
        return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3"

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        if self.code[option - 1] == 'O':
            self.code[option - 1] = 'X'
        else:
            self.code[option - 1] = 'O'
        print(self.code)

        if self.code == ['O', 'O', 'O']:
            print(self.code)
            self.unlocked = True
            return "You entered the correct code!"
        else:
            return "The number of correct characters."

    def is_unlocked(self):
        return self.unlocked

    def clue(self):
        return "Try again."

    def success(self):
        return "Congratulations! You've successfully opened the door!"

