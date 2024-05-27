import random
from door import Door

class ComboDoor(Door):

    def __init__(self):
        self.combination = random.randint(1, 10)
        self.unlocked = False

    def examine_door(self):
        return "A door with a combination lock. You can spin the dial to a number 1-10."

    def menu_options(self):
        return "Enter # 1-10:"

    def get_menu_max(self):
        return 10

    def attempt(self, option):
        if option == self.combination:
            self.unlocked = True
            return "You entered the correct combination!"
        elif option < self.combination:
            return "Too low."
        else:
            return "Too high."

    def is_unlocked(self):
        return self.unlocked

    def clue(self):
        return "Try another number."

    def success(self):
        return "Congratulations! You've successfully opened the door!"
