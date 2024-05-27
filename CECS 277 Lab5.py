from check_input import get_yes_no 
#from Die import Die
from Player import Player

def take_turn(player):

    player.roll_dice()
    print("Dice:", player)
    if player.has_three_of_a_kind():
        print("Three of a kind!")
    elif player.has_pair():
        print("Pair!")
    elif player.has_series():
        print("Series!")
    else:
        print("Aww. Too Bad.\n")
    print("Points:", player.get_points())

def main():
    
    print("-Yahtzee-\n")
    player = Player()
    while True:
        take_turn(player)
        if not get_yes_no("\nContinue playing? (y/n): "):
            break
    print("Game Over.\nFinal Score =", player.get_points())

if __name__ == "__main__":
    main()
