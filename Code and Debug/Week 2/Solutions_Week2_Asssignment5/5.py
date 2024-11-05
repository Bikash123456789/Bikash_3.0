def addDigits(n):
    sum = 0
    while n > 0:
        remainder = n % 10
        sum = sum + remainder
        n = n // 10
    return sum


print(addDigits(123))
print(addDigits(58714))
