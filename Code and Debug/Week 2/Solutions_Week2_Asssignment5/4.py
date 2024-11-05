def pattern(x, n):
    i = 1
    power = 1
    sum = 0
    while i <= n:
        if i % 2 == 0:
            sum = sum - x**power
        else:
            sum = sum + x**power
        power += 2
        i += 1

    return sum


print(pattern(6, 4))
