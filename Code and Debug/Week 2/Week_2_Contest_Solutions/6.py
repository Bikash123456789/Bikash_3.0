def sumOfSquares(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i**2
        i += 1
    return sum


print(sumOfSquares(5))
