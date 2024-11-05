def sum(n1: int, n2: int) -> int:
    i = 1
    sum = 0
    while i <= n1:
        if i % 3 == 0:
            sum = sum + i
        i = i + 1
    return sum


print(sum(10, 3))
