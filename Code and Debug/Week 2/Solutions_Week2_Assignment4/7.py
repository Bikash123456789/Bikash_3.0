def pattern(n: int) -> int:
    i = 1
    while i <= n:
        print(f"{i**2}", end=" ")
        i = i + 1


pattern(10)
