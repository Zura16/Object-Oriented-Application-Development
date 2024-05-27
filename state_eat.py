from puppy_state import PuppyState
from state_play import StatePlay
from state_asleep import StateAsleep

class StateEat(PuppyState):

    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feeds < 3:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(StateAsleep())
            return "The puppy ate so much it fell asleep!"

    def play(self, puppy):
        puppy.reset()  
        return "The puppy looks up from its food and chases the ball you threw."
