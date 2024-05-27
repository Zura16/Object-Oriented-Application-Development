from character import Character

class Elf(Character):

    def __init__(self, name):
        super().__init__(name)

    def abilities(self):
        return {"Archery": 1, "Fighting": 0, "Fire Magic": 0, "Healing": 0}

    def constitution(self):
        return 13

    def strength(self):
        return 10

    def wisdom(self):
        return 15
