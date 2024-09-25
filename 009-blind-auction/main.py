import os
from art import logo

def main():
    print(logo)
    should_continue = True
    bid_dict = {}
    while should_continue:
        key = input("What is your name?: ")
        value = int(input("What is your bid?: $"))
        bid_dict[key] = value
        continue_text = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if continue_text == "no": should_continue = False
        else: os.system('cls')
    os.system('cls')
    winner, max_bid = get_max(bid_dict)
    print(f"The winner is {winner} with a bid of ${max_bid}")

def get_max(my_dict):
    max_value = 0
    winner = ""
    for key in my_dict:
        if max_value < my_dict[key]:
            max_value = my_dict[key]
            winner = key
    return winner, max_value

main()