"""
1. Ordered
2. Mutable ( which can be changed )
3. 
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]


# a[0] = 100
# a[-1] = 100
# print(a)


for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = 1
    else:
        a[i] = -1

print(a)
