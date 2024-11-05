def factorial(n: int) -> int:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact


def sumPattern(n: int) -> int:
    i = 1
    sum = 0
    while i <= n:
        sum = sum + 1 / factorial(i)
        i += 1
    return sum


print(sumPattern(5))
