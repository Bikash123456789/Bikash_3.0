def sum(a, b):
    i = a
    sum = 0
    while i <= b:
        sum = sum + i
        i = i + 1
    return sum


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 > n2:
    print("n1 should be smaller than n2")
else:
    print(sum(n1, n2))
