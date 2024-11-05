def printPattern(n):
    if n >= 0:
        start = -n
        end = n
    else:
        start = n
        end = -n
    i = start
    while i <= end:
        print(i, end=" ")
        i = i + 1


printPattern(15)
