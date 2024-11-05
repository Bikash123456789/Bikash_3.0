a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

count = 0
for ele in a:
    if ele % 5 == 0:
        count += 1

print(count)
