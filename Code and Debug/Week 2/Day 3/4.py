n = int(input("Enter the number: "))


def print1toN(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1

    print()


print1toN(10)
print1toN(5)
