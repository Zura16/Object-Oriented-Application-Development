from random import randint
from entity import Entity

class Dragon(Entity):
    
    def basic_attack(self, hero):
        damage = randint(3, 7)
        hero.take_damage(damage)
        return f"{self._name} smashes you with its tail for {damage} damage!"

    def special_attack(self, hero):
        damage = randint(4, 8)
        hero.take_damage(damage)
        return f"{self._name} slashes you with its claws for {damage} damage!"