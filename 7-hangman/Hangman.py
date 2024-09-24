# Hangman project
# import random
from hangman_art import logo, hangman_phases
from english_words import get_english_words_set

def main():
    print(logo)
    # words_list = ["aardvark", "baboon", "camel", "babe", "madisita"]
    words_list = get_english_words_set(['web2'], lower=True)
    # chosen_word = random.choice(words_list)
    chosen_word = words_list.pop()
    placeholder = ["_"] * len(chosen_word)
    hangman = hangman_phases
    hangman.reverse()
    starting_lives = len(hangman) - 1
    current_lives = starting_lives
    letters_used = []
    while current_lives > 0 and "_" in placeholder:
        print(f"Letters used: {letters_used}")
        letter_guessed, guess_result = guess_letters(chosen_word, placeholder)
        if letter_guessed in letters_used:
            print("Letter was already used. Please choose a different letter")
            continue
        else:
            letters_used.append(letter_guessed)
            if not guess_result:
                print(f"You guessed \"{letter_guessed}\", that's not in the word\n{hangman[current_lives - 1]}")
                current_lives -= 1
            else:
                print(hangman[current_lives])
            print("*" * 30 + f"{current_lives}/{starting_lives} LIVES LEFT" + "*" * 30)
    if(current_lives > 0):
        print("YOU WIN!")
    else:
        print(f"YOU LOSE :( the word to guess was {chosen_word}")

def step_1(chosen_word):
    # random.choice can be used instead
    # chosen_word = words_list[random.randint(0,(len(words_list)-1))]
    print(chosen_word)

    display = ""

    guess = input("Guess a letter for the selected word\n").lower()
    for letter in chosen_word:
        if guess == letter:
            # print("Right")
            display += letter
        else:
            # print("Wrong")
            display += "_"
         
def guess_letters(chosen_word, placeholder):
    print("Word to guess: " + "".join(placeholder))
    guess = input("Guess a letter: ").lower()
    i = 0
    was_guess_correct = False
    for letter in chosen_word:
        if letter == guess:
            placeholder[i] = guess
            was_guess_correct = True
        i += 1
    print("".join(placeholder))
    return guess, was_guess_correct
            
main()