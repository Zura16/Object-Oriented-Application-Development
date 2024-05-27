import random
import check_input

def read_file(file_name):
    states = []
    with open("statecapitals.txt") as file_name:
        for line in file_name:
            state, capital = line.strip().split(',')
            states.append([state, capital])
    return states

def get_random_state(states):
    return random.choice(states)

def get_random_choices(states, correct_choice):
    choices = [correct_choice]

    while len(choices) < 4:
        random_choice = random.choice(states)[1]

        if random_choice not in choices and random_choice != correct_choice:
            choices.append(random_choice)

    random.shuffle(choices)
    return choices

def ask_question(correct_state, possible_answers):

    print("\nWhat is the capital of {}? ".format(correct_state))

    options = ['A', 'B', 'C', 'D', '\n']

    print("\t".join(["{}. {}".format(options[i], possible_answers[i]) for i in range(4)]))

    user_choice = input("Enter your choice (A, B, C, or D): ").upper()

    while user_choice not in options:
        print("Invalid choice. Please enter A, B, C, or D. ")
        user_choice = input("Enter your choice (A, B, C, or D):  ").upper()
    return options.index(user_choice)

def main():
    file_name = 'statecapitals.txt'
    states = read_file(file_name)
    total_points = 0

    for _ in range(10):
        correct_state, correct_capital = get_random_state(states)
        choices = get_random_choices(states, correct_capital)
        correct_choice = ask_question(correct_state, choices)

        if correct_choice == choices.index(correct_capital):
            print("Correct!")
            total_points += 1
        else:
            print("Incorrect. The correct answer was: {} \n ".format(correct_capital))

    print("End of test. You got {} correct. \n ".format(total_points))

if __name__ == "__main__":
    main()

