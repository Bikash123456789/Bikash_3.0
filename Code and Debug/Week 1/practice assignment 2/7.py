sal = int(input("Enter the amount of salary\n"))
increment = 0

if sal < 10000:
    increment = 5 * sal / 100
elif 10000 <= sal <= 20000:
    increment = 10 * sal / 100
elif 20000 <= sal <= 50000:
    increment = 15 * sal / 100
else:
    increment = 20 * sal / 100

print("The updated salary is", sal + increment)
