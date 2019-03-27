"""
Every integer greater than 1 can be uniquely expressed as the product of
prime numbers (ignoring reordering those numbers). This is called the
prime factorisation of the number.

For example:
 * 100 = 2 * 2 * 5 * 5
 * 101 = 101 (since 101 is a prime number)

We are interested in the product of the distinct prime factors of a given
number; in other words each number in the prime factorisation is to be used
only once. Since 100 = 2 2 5 5 the product we require is 10 (i.e. 2
5). Write a program which reads in a single integer n (1 < n < 1,000,000)
and outputs a single integer, the product of the distinct prime factors of n.
"""

def product_of_unique_factors(n: int) -> int:
    factors = set()
    current_factor = 2

    # Divides the factor out of n every time it finds one
    while n > 1:
        if n % current_factor  == 0:
            factors.add(current_factor)
        else:
            current_factor += 1

    # When n reaches 1, all factors have been removed
    product = 1
    for i in factors:
        product *= i

    return product


def main():
    n = int(input("Enter number to find product of unique prime factors: "))

    if n < 1 or n > 1000000:
        print("Number out of range")
        return

    print(product_of_unique_factors(n), "is the product of unique prime factors of", n)


if __name__ == "__main__":
    main()