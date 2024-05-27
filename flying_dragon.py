from dragon import Dragon
from random import randint

class FlyingDragon(Dragon):

    def __init__(self, name, max_hp, swoops):
        super().__init__(name, max_hp)
        self._swoops = swoops

    def special_attack(self, hero):
        if self._swoops > 0:
            damage = randint(5, 8)
            hero.take_damage(damage)
            self._swoops -= 1
            return f"{self._name} swoops at you for {damage} damage!"
        else:
            return f"{self._name} tries to swoop down to hit you, but failed."

    def __str__(self):
        return super().__str__() + f" \nswoop shots remaining: {self._swoops}"