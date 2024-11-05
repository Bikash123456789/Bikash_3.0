"""
Ask a number from user = 50
-50 to 50

Ask a number from user = 10
-10 to 10

Ask a number from user = -13
13 to -13

Ask a number from user = -20
20 to -20

"""

n = int(input("Enter a number: "))


if n > 0:
    i = (-1) * n
    while i <= n:
        print(i, end=" ")
        i = i + 1
else:
    i = (-1) * n
    while i >= n:
        print(i, end=" ")
        i = i - 1
