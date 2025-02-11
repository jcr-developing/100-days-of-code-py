import art
from game_data import data
import random
import console_gb as cgb

def main():
    score = 0
    current_list = []
    while len(data) > 0:
        init_display()
        if score != 0:
            print(f"You're right! Current score: {score}.")
        get_data_to_compare(current_list, data, 2)
        print_game_info(current_list)
        new_score = compare_user_guess(current_list, score)
        if new_score == score:
            init_display()
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        else:
            score = new_score
    init_display()
    print("You made it through all the options! You're the...")
    print(art.champion)

def init_display():
    cgb.clear_console()
    print(art.logo)

def get_data_to_compare(current_list, original_data, size: int):
    """Receives a current_list that if empty, 'size' random entries will be added; if not, elements will be
    appended until reaching the specified size. Elements appended to the current_list will be popped out
    (removed) from the original_data"""
    current_size = len(current_list)
    if current_size < size:
        for _ in range(size - current_size):
            random_pos = random.randrange(len(original_data))
            current_list.append(original_data[random_pos])
            original_data.pop(random_pos)
    # print(current_list)

def print_game_info(data_to_guess):
    a = data_to_guess[0]
    b = data_to_guess[1]
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(art.vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.")

def compare_user_guess(current_list, score):
    options = {"a": 0, "b": 1}
    user_guess = cgb.get_controlled_user_input(
        "Who has more followers? Type 'A' or 'B': ", options, "Please type a valid option.",
        True, True)
    user_guess_data = current_list[user_guess]
    for i in range(len(current_list)):
        if i == user_guess:
            continue
        else:
            rival = current_list[i]
            # Only if guess is lower, then the game ends
            if user_guess_data["follower_count"] < rival["follower_count"]:
                return score
            else:
                current_list.pop(i)
                return score + 1

main()