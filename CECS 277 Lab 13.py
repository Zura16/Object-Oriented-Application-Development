from puppy import Puppy
from check_input import get_int_range

def main():
    print("Congratulations on your new puppy!")
    puppy = Puppy()

    while True:
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")

        choice = get_int_range("Enter choice: ", 1, 3)

        if choice == 1:
            print(puppy.give_food())
        elif choice == 2:
            print(puppy.throw_ball())
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
