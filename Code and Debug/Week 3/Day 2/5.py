n = 11
m = n // 2 + 1
o = n // 2
for i in range(1, m + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


for i in range(1, o):
    for j in range(1, m - i):
        print(j, end="")
    print()
