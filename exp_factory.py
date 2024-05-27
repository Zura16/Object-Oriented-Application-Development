from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random

class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        if random.randint(0, 1) == 0:
            return ExpGoblin()
        else:
            return ExpTroll()