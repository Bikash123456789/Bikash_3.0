# Iterating elements

a = [78.45, 56, 23, 34, 56]

print(f"The length of array a is {len(a)}")

for i in range(0, len(a)):
    print(a[i], end=" ")

print()


# Reverse
# for i in range(-1, -(len(a) + 1), -1):
#     print(a[i], end=" ")

for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
