num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))


def average(a, b, c):
    return (a + b + c) // 3


avg = average(num1, num2, num3)

print(f"The average of {num1},{num2} and {num3} is {avg}")
if avg >= num4:
    print(f"{avg} is greater than {num4}")
else:
    print(f"{avg} is smaller than {num4}")
