def checkPrime(n: int) -> int:
    if n == 1:
        return False
    i = 2
    check = True
    while i < n:
        if n % i == 0:
            check = False
            break
        i += 1

    return check


def printPrimeFactors(n: int):
    i = 1
    while i <= n:
        if n % i == 0 and checkPrime(i):
            print(i, end=" ")
        i += 1


printPrimeFactors(72)
