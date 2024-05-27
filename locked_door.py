import random
from door import Door

class LockedDoor(Door):

    def __init__(self):
        self.key_location = random.randint(1,3)
        self.input = 0

    def examine_door(self):
        return "A locked door. The key is hidden nearby."

    def menu_options(self):
        return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock"

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        self.input = option
        if self.input == 1 and self.key_location == 1:
            return "You looked under the mat and found the key!"
        
        elif self.input == 2 and self.key_location == 2:
            return "You looked behind the painting and found the key!"
        
        elif self.input == 3 and self.key_location == 3:
            return "You looked inside the book and found the key!" 
            
        else:
            return "You found nothing. Keep looking."

    def is_unlocked(self):
        return self.input == self.key_location

    def clue(self):
        return "Look somewhere else."

    def success(self):
        return "Congratulations! You've successfully opened the door!"
