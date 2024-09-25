import random
import art
import os

outcome_msgs = {
    "w": "You win! 😀",
    "d": "It's a draw! 😑",
    "l": "You lost 🥴",
    "w21": "You win with a Blackjack! 😎🥳",
    "d_over": "Your opponent went over. You win! 😁",
    "u_over": "You went over. you lose! 😭",
}

def main():
    os.system('cls')
    again = do_user_wanna_play()
    while again:
        os.system('cls')
        print(art.logo)
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # cards = [11, 8, 3] * 5
        user_cards = []
        dealer_cards = []
        draw_cards(deck, 2, dealer_cards)
        draw_cards(deck, 2, user_cards)
        user_score, dealer_score = turn_summary(user_cards, dealer_cards)
        is_first_additional_card_needed = is_card_needed(user_score)
        if is_first_additional_card_needed:
            is_extra_card_needed = ask_if_continue()
        else:
            is_extra_card_needed = False
        # user cycle
        while is_extra_card_needed:
            draw_cards(deck, 1, user_cards)
            user_score, dealer_score = turn_summary(user_cards, dealer_cards)
            if is_card_needed(user_score):
                is_extra_card_needed = ask_if_continue()
            else:
                is_extra_card_needed = False
        # dealer cycle
        while dealer_score < 17 and is_first_additional_card_needed and user_score < 22:
            draw_cards(deck, 1, dealer_cards)
            dealer_score = blackjack_sum(dealer_cards)
        turn_summary(user_cards, dealer_cards, True, is_first_additional_card_needed)
        again = do_user_wanna_play()

def draw_cards(cards, amount, current_cards):
    for x in range(amount):
        current_cards.append(random.choice(cards))

def blackjack_sum(cards_on_hand, use_list_comprehension = True, old = 11, new = 1):
    if sum(cards_on_hand) > 21 and 11 in cards_on_hand:
        if use_list_comprehension:
            # By assigning a new list to the parameter cards_on_hand, the original list outside
            # the function is not affected.
            cards_on_hand[:] = [original if original != 11 else 1 for original in cards_on_hand]
            return sum(cards_on_hand)
        else:
            """Replace elements inplace"""
            # Affecting a specific element of the list passed as a parameter, updates
            # the original list outside the  function
            i = -1
            try:
                i = cards_on_hand.index(old, i + 1)
                cards_on_hand[i] = new
            except ValueError:
                pass
            return sum(cards_on_hand)
    else:
        return sum(cards_on_hand)

def is_card_needed(cards_score):
    if cards_score > 20:
        # Game over
        return False
    else:
        return True

def turn_summary(user_cards, dealer_cards, is_game_over = False, was_first_additional_card_needed = True):
    user_sum = blackjack_sum(user_cards)
    dealer_sum = blackjack_sum(dealer_cards)
    if not is_game_over:
        print(f"*****Your cards: {user_cards}. Current score: {user_sum}")
        print(f"*****Computer first card: {dealer_cards[0]}")
        return user_sum, dealer_sum
    else:
        print(f"---Your final hand: {user_cards}. Final score: {user_sum}")
        print(f"---Computer's final hand: {dealer_cards}. Final score {dealer_sum}")
        if user_sum > 21:
            print(outcome_msgs["u_over"])
        elif dealer_sum > 21:
            print(outcome_msgs["d_over"])
        elif user_sum == 21 and was_first_additional_card_needed == False:
            print(outcome_msgs["w21"])
        elif user_sum == dealer_sum:
            print(outcome_msgs["d"])
        elif user_sum > dealer_sum:
            print(outcome_msgs["w"])
        elif user_sum < dealer_sum:
            print(outcome_msgs["l"])
        else:
            print("I do not know what happened :(")

def ask_if_continue():
    while True:
        response = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please, only type either 'y' or 'n'")

def do_user_wanna_play():
    while True:
        response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please, only type either 'y' or 'n'")

main()