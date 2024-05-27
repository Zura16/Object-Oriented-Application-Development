from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def abilities(self):
        pass

    @abstractmethod
    def constitution(self):
        pass

    @abstractmethod
    def strength(self):
        pass

    @abstractmethod
    def wisdom(self):
        pass

    def __str__(self):
        abilities_str = "\n".join([f"{ability}: Level {level}" for ability, level in self.abilities().items()])
        stats_str = f"\n-Stats-\nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}"
        return f"{self.name}\n-Abilities-\n{abilities_str}{stats_str}"
