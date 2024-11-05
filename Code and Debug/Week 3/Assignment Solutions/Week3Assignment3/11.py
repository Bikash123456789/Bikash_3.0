def isPrime(n):
    isPrime = True
    i = 2
    while i < n:
        if n % i == 0:
            isPrime = False
        i += 1
    return isPrime


def calculatePrime(lst):
    for ele in lst:
        if isPrime(ele):
            print(ele, end=" ")


a = [34, 11, 91, 59, 33, 22]

calculatePrime(a)
# print(isPrime(91))
