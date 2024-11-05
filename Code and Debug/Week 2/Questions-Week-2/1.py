def maxi(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the largest")
    elif b >= a and b >= c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")


def mini(a, b, c):
    if a <= b and a <= c:
        print(f"{a} is the smallest")
    elif b <= a and b <= c:
        print(f"{b} is the smallest")
    else:
        print(f"{c} is the smallest")


num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

maxi(num1, num2, num3)
mini(num1, num2, num3)
