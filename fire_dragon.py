from dragon import Dragon
from random import randint

class FireDragon(Dragon):

    def __init__(self, name, max_hp, f_shots):
        super().__init__(name, max_hp)
        self._fire_shots = f_shots

    def special_attack(self, hero):
        if self._fire_shots > 0:
            damage = randint(5, 9)
            hero.take_damage(damage)
            self._fire_shots -= 1
            return f"{self._name} engulfs you in flames for {damage} damage!"
        else:
            return f"{self._name} tries to spit fire at you but is all out of fire shots."

    def __str__(self):
        return super().__str__() + f" \nfire shots remaining: {self._fire_shots}"