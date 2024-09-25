# On this script, trial division algorithm is used as the chosen primality test
import math

def is_prime(num):
    # By definition a prime number is a natural number greater than one
    if num > 1:
        if isinstance(num, float):
            if num.is_integer():
                return trial_div(num)
            else:
                return False
        elif isinstance(num, int):
            return trial_div(num)
        else:
            return False
    else:
        return False

def trial_div(num):
    middle_point = math.floor(math.sqrt(num)) + 1
    for div in range(2, middle_point):
        if num % div == 0:
            return False
    return True

while True:
    x = float(input("Please type a number to check primality: "))
    if is_prime(x):
        print(f"{x} IS PRIME!")
    else:
        print(f"{x} IS NOT PRIME!")