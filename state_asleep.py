from puppy_state import PuppyState
from state_eat import StateEat

class StateAsleep(PuppyState):
    def feed(self, puppy):
        """Handle feeding the puppy when it is asleep."""
        puppy.inc_feeds()
        puppy.reset()  
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        """Handle playing with the puppy when it is asleep."""
        return "The puppy is asleep. It doesn't want to play right now."
