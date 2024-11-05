num1 = int(input("Enter the first Number\n"))
num2 = int(input("Enter the second Number\n"))
num3 = int(input("Enter the third Number\n"))
num4 = int(input("Enter the fourth Number\n"))

if num1 < num2 and num1 < num3 and num1 < num4:
    print(f"{num1} is the smallest")
elif num2 < num3 and num2 < num4:
    print(f"{num2} is the smallest")
elif num3 < num4:
    print(f"{num3} is the smallest")
else:
    print(f"{num4} is the smallest")
