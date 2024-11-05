p = 10
n = p // 2 + 1
m = p // 2

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, m + 1):
    for j in range(1, m - i + 2):
        print(j, end=" ")
    print()
