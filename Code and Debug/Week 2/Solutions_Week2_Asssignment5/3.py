def pattern(x, n):
    i = 1
    output = 0
    div = 1
    while i <= n:
        output += x / div
        div += 2
        i += 1

    return output


print(pattern(9, 11))
