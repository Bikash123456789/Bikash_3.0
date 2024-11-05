a = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(a)):
    if i % 2 == 0:
        a[i] = 1
    else:
        a[i] = -1

print(a)
