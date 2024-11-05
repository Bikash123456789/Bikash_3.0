def pattern1(n: int) -> int:
    i = 1
    while i <= n:
        print(f"{i*10}", end=" ")
        i += 1
    print()


def pattern2(n: int) -> int:
    i = 0
    while i < n:
        print(f"{2**i}", end=" ")
        i += 1
    print()


pattern1(4)

pattern2(7)
