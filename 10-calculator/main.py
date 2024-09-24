import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def get_float_number(instructions):
    while True:
        possible_number = input(instructions)
        try:
            return float(possible_number)
        except:
            print("Please type a valid number")

def get_operation():
    while True:
        selection = input("+\n-\n*\n/\nPick an operation: ").strip()
        if selection == "+":
            return add, selection
        elif selection == "-":
            return subtract, selection
        elif selection == "*":
            return multiply, selection
        elif selection == "/":
            return divide, selection
        else:
            print("Please select a valid operation")

def get_operation_with_dict():
    print("Using dictionaries")
    op_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    selection = input("+\n-\n*\n/\nPick an operation: ").strip()
    while True:
        if selection in op_dict.keys():
            return op_dict[selection], selection
        else:
            print("Please select a valid operation")

def ask_if_continue(current_total):
    answer = input(
        f"Type 'y' to continue calculating with {current_total}, or 'n' to start a new calculation: ").lower().strip()
    while True:
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            answer = input("Please type 'y' or 'n' only: ")

def main():
    os.system('cls')
    print(art.logo)
    should_continue = True
    total = get_float_number("What's the first number?: ")
    while should_continue:
        n1 = total
        # Select operation
        operation, op_str = get_operation_with_dict()
        # Write second number
        n2 = get_float_number("What's the next number?: ")
        # Make the appropriate operation
        total = operation(n1, n2)
        print(f"{n1} {op_str} {n2} = {total}")
        should_continue = ask_if_continue(total)
    main()

main()