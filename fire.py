from decorator import Decorator

class Fire(Decorator):
    def __init__(self, character):
        super().__init__(character)

    def abilities(self):
        abilities = self.character.abilities()
        abilities["Fire Magic"] += 1
        return abilities

    def constitution(self):
        return self.character.constitution() - 3

    def strength(self):
        return self.character.strength() - 1

    def wisdom(self):
        return self.character.wisdom() + 5
