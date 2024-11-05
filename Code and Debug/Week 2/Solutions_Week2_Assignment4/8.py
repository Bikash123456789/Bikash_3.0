"""
Q9. Ask a number from user. Print if that number is prime or not, use 
functions.
 Q10. Ask a number from user n1. From 1 to n1, print how many prime 
numbers are there
"""


def isPrime(n: int) -> bool:
    if n == 1:
        return False
    i = 2
    check = True
    while i < n:
        if n % i == 0:
            check = False
            break
        i = i + 1
    return check


print(isPrime(42))
print(isPrime(41))


def printPrime(n: int) -> None:
    i = 1
    while i <= n:
        if isPrime(i):
            print(i, end=" ")
        i = i + 1


printPrime(40)
