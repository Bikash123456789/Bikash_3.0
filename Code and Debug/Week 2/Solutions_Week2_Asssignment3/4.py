n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))


def calSum(n1, n2):
    i = n1
    sum = 0
    while i <= n2:
        if i % 5 == 0:
            sum += i
        i = i + 1
    return sum


if n1 > n2:
    print("n1 should be smaller than n2")
else:
    print(calSum(n1, n2))
