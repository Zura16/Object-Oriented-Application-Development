# archery.py

from decorator import Decorator

class Archery(Decorator):
    """Decorator class for adding Archery ability to a character."""

    def __init__(self, character):
        """Initialize the Archery decorator."""
        super().__init__(character)

    def abilities(self):
        """Add Archery ability to the character."""
        abilities = self.character.abilities()
        abilities["Archery"] += 1
        return abilities

    def constitution(self):
        """Adjust constitution stat based on Archery ability."""
        return self.character.constitution() - 2

    def strength(self):
        """Adjust strength stat based on Archery ability."""
        return self.character.strength() + 5

    def wisdom(self):
        """Adjust wisdom stat based on Archery ability."""
        return self.character.wisdom() - 2
