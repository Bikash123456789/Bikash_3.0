for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print(i, end=" ")
    print()


for i in range(1, 5):
    for k in range(1, i + 1):
        print(" ", end=" ")
    for j in range(1, 2 * (5 - i)):
        print(5 - i, end=" ")
    print()
