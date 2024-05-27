from character import Character

class Halfling(Character):

    def __init__(self, name):
        super().__init__(name)

    def abilities(self):
        return {"Archery": 0, "Fighting": 0, "Fire Magic": 0, "Healing": 1}

    def constitution(self):
        return 15

    def strength(self):
        return 10

    def wisdom(self):
        return 13
