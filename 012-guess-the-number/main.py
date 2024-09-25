from art import logo
import random
from os import system, name
import global_constants as gc

def main():
    clear_console()
    print(logo)
    num_to_guess = print_instructions()
    attempts = get_num_of_attempts()
    user_guess(attempts, num_to_guess)
    if ask_play_again():
        main()

def print_instructions():
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between {gc.LOWER_LIMIT} and {gc.UPPER_LIMIT}")
    return random.randint(gc.LOWER_LIMIT, gc.UPPER_LIMIT)

def get_num_of_attempts():
    while True:
        level = get_clean_input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == gc.EASY_DESC:
            return gc.EASY_ATTEMPTS
        elif level == gc.HARD_DESC:
            return gc.HARD_ATTEMPTS
        else:
            print("Please type a valid level")

def ask_play_again():
    while True:
        response = get_clean_input("Do you want to play again? Type 'y' or 'n': ")
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please type a valid option")

def get_clean_input(prompt: str):
    return input(prompt).lower().strip()

# source: https://stackoverflow.com/a/684344
def clear_console():
    system('cls' if name == 'nt' else 'clear')

def user_guess(max_attempts, num_to_guess):
    for i in range(0, max_attempts):
        print(f"You have {max_attempts - i} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        try:
            guess = float(guess)
        except ValueError:
            print("Guess again")
            continue
        if guess == num_to_guess:
            print(f"You got it! the answer was {num_to_guess}")
            return
        elif guess > num_to_guess:
            print("Too high.")
        else:
            print("Too low.")
    print(f"You've run out of guesses, you lose. The hidden number was {num_to_guess}")

main()