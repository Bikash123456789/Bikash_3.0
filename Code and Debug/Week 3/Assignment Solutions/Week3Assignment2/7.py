p = 9
n = p // 2 + 1
m = p // 2

for i in range(1, n + 1):
    for k in range(1, n - i + 1):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print(j, end=" ")
    print()

for i in range(1, m + 1):
    for k in range(1, i + 1):
        print(" ", end=" ")
    for j in range(1, 2 * (m - i + 1)):
        print(j, end=" ")
    print()
