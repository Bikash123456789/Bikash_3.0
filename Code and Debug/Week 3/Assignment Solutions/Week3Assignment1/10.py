for i in range(1, 6):
    for j in range(1, 6 - i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()