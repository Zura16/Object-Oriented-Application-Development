# Aalind Kale
# Emmanuel Moye
# Group 16
# CECS 277
# Lab 1 - Python Basics


import check_input

import random

def shell_game_():
    money = 100
    
    while money > 0:
        print(f"\nYou currently have ${money}")
        
        # Randomly place the ball under one of the shells
        ball_position = random.randint(1, 3)
        
        # Get the user's bet
        bet_amount = check_input.get_int_range("Bet amount? ", 1, money)
        
        # Get the user's guess 
        
        print('  ___     ___     ___ ')
        print(' /   \\   /   \\   /   \\')
        print('/  1  \\ /  2  \\ /  3  \\')
        print('------- ------- -------')
        guess = int(input("Guess the location of the ball (1-3): "))
    
        if 1 <= guess <= 3:
            if ball_position == 1:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/  o  \\ /     \\ /     \\')
                print('------- ------- -------')

            elif ball_position == 2:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/     \\ /  o  \\ /     \\')
                print('------- ------- -------')

            elif ball_position == 3:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/     \\ /     \\ /  o  \\')
                print('------- ------- -------')


            
        else:
            print("Invalid guess. Please enter a number between 1 and 3. ")

        # Check if the guess is correct
        if guess == ball_position:
            money += bet_amount
            print(f"Congratulations! The ball was under shell {ball_position}. You won ${2 * bet_amount}.")
        else:
            money -= bet_amount
            print(f"Sorry, the ball was under shell {ball_position}. You lost ${bet_amount}.")

            if money == 0:
                break

            
            
        # Ask the user if they want to play again
        play_again = check_input.get_yes_no("Do you want to play again? (Y/N): ")

        if play_again != 'y':
            pass
        else:
            print("Thank you for playing!")
            break

    print("You are out of money! Game over.")

if __name__ == "__main__":
    shell_game_()
