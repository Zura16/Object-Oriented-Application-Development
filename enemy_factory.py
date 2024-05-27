import abc

class EnemyFactory(abc.ABC):
    @abc.abstractmethod
    def create_random_enemy(self):
        pass

# beg_factory.py
from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
import random

class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        if random.randint(0, 1) == 0:
            return BegGoblin()
        else:
            return BegTroll()