def printfactors(n):
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i = i + 1


def numOfFactors(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i = i + 1
    return count


def isPrime(n):
    if numOfFactors(n) == 2:
        return True
    return False


if isPrime(31):
    print("Prime")
else:
    print("Not prime")
