"""

Ask M from User
Ask N from User

If M < N -> M to N
If M > N -> N to M
"""

m = int(input("Enter the number M: "))
n = int(input("Enter the number N: "))

if m <= n:
    i = m
    while i <= n:
        print(i, end=" ")
        i = i + 1
else:
    i = n
    while i <= m:
        print(i, end=" ")
        i = i + 1
