"""
Q3. Create a function named factorial which takes a integer as an input and 
returns the factorial of that number.
"""


def fact(n: int) -> int:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial


print(fact(5))
