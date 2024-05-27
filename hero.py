from entity import Entity
import random

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 25)

    def melee_attack(self, enemy):
        dmg = sum(random.randint(1, 6) for _ in range(2))
        enemy.take_damage(dmg)
        return f"{self._name} slashes {enemy.name} with a sword for {dmg} damage."

    def ranged_attack(self, enemy):
        dmg = random.randint(1, 12)
        enemy.take_damage(dmg)
        return f"{self._name} pierces {enemy.name} with an arrow for {dmg} damage."
