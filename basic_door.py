import random
from door import Door

class BasicDoor(Door):

    def __init__(self):
        self.state = random.choice(["push", "pull"])
        self.unlocked = False

    def examine_door(self):
        return "A door that is either pushed to open, or pulled."

    def menu_options(self):
        return "1. Push\n2. Pull"

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        if option == 1 and self.state == "push" or option == 2 and self.state == "pull":
            self.unlocked = True
            return "You successfully opened the door!"
        else:
            return "You try the other way."

    def is_unlocked(self):
        return self.unlocked

    def clue(self):
        return "Try the other way."

    def success(self):
        return "Congratulations! You've successfully opened the door!"
