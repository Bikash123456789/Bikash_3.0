def factorial(n: int) -> int:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact


print(factorial(5))


