"""
Q1. Create a function named as checkPrime that takes an integer as an 
argument. Print YES if the number passed is a prime number else print NO.
"""


def checkPrime(n: int) -> int:
    i = 2
    check = True
    while i < n:
        if n % i == 0:
            check = False
            break
        i += 1

    return check


print(checkPrime(17))
