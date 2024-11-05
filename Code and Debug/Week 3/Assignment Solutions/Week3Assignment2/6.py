p = 9
n = p // 2 + 1
m = p // 2

for i in range(1, n + 1):
    for j in range(n - i + 1, n + 1):
        print(j, end=" ")
    print()

for i in range(1, m + 1):
    for j in range(i + 1, m + 2):
        print(j, end=" ")
    print()
