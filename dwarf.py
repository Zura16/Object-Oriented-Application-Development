from character import Character

class Dwarf(Character):

    def __init__(self, name):
        super().__init__(name)

    def abilities(self):
        return {"Archery": 0, "Fighting": 1, "Fire Magic": 0, "Healing": 0}

    def constitution(self):
        return 13

    def strength(self):
        return 15

    def wisdom(self):
        return 10
