"""
Write a program that, given a number greater than 2, returns if it is a
prime number or not. We can assume that the computer at the start knows
only that 2 is prime number. We should use a loop to test several numbers.
"""

import math

def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Enter a number: "))

    if is_prime(n):
        print(n, "is prime")
    else:
        print(n, "is not prime")

if __name__ == "__main__":
    main()