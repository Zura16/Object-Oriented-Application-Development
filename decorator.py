from character import Character
from abc import ABC, abstractmethod

class Decorator(Character):

    def __init__(self, character):
        super().__init__(character.name)
        self.character = character

    def abilities(self):
        return self.character.abilities()

    def constitution(self):
        return self.character.constitution()

    def strength(self):
        return self.character.strength()

    def wisdom(self):
        return self.character.wisdom()
