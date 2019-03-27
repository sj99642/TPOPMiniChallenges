"""
A prime number (or a prime) is a natural number greater than 1 that has
no positive divisors other than 1 and itself.

The property of being prime is called primality. A simple but slow method of
verifying the primality of a given number is known as trial division. It
consists of testing whether n is a multiple of any integer between 2 and sqrt(n).

# The Basic

Write a program that, given a number comprised between 2 and 49, returns
if it is a prime number or not. We can assume that the computer knows
(stores) that [2, 3, 5, 7] are prime numbers.
"""

def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False

    return True

def main():
    n = int(input("Enter number between 2 and 49: "))

    if n < 2 or n > 49:
        print("Number out of range")
        return

    if is_prime(n):
        print(n, "is prime")
    else:
        print(n, "is not prime")

if __name__ == "__main__":
    main()