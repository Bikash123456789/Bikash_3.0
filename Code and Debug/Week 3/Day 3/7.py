# Traverse by value

a = [78, 67, 44, -100, 87, 33, 31]

for i in a:
    print(i, end=" ")


# Traverse by both index/value

for index, value in enumerate(a):
    print(index, value)
