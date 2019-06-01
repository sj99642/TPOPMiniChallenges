"""
Write a program that, given a number greater than 2, returns if it is a
prime number or not. We can assume that the computer at the start knows
only that 2 is prime number. Every time the program is ran, it should
remember the prime numbers it has found before.
"""

import math

def is_prime(n: int) -> bool:
    with open("Clever_FoundPrimes.txt", "rt") as file:
        primes = [int(x) for x in file.readlines()]

    # Has a list of currently found primes
    if n in primes:
        return True

    # Now find if it is prime manually
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    # It is a prime
    with open("Clever_FoundPrimes.txt", "at") as file:
        file.write(str(n) + "\n")
    return True


def main():
    n = int(input("Enter a number: "))

    if is_prime(n):
        print(n, "is prime")
    else:
        print(n, "is not prime")

if __name__ == "__main__":
    main()