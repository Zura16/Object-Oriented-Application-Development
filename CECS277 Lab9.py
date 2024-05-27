from maze import Maze
from hero2 import Hero
from minotaur import Minotaur

def main():
    
    maze = Maze()
    hero = Hero()
    minotaur = Minotaur()

    print("Welcome to Minotaur's Maze!\n")
    print("Use the following keys to move:")
    print("'w' - Up, 's' - Down, 'a' - Left, 'd' - Right\n")

    while True:
        print(maze)  
        direction = input("Enter direction to move (w/a/s/d): ").lower()

        if direction == 'w':
            result = hero.go_up()
        elif direction == 's':
            result = hero.go_down()
        elif direction == 'a':
            result = hero.go_left()
        elif direction == 'd':
            result = hero.go_right()
        else:
            print("Invalid input. Please enter 'w', 'a', 's', or 'd'.")
            continue

        if result == 'f':
            print("Congratulations! You reached the exit. You win!")
            break
        elif result == 'M':
            print("Oh no! You were captured by the minotaur. Game over!")
            break
        elif result == '*':
            print("You hit a wall. Try a different direction.")
        else:
            result_minotaur = minotaur.move_minotaur()
            if result_minotaur == 'H':
                print("Oh no! You were captured by the minotaur. Game over!")
                break

if __name__ == "__main__":
    main()
