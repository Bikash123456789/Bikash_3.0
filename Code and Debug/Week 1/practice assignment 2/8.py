year = int(input("Enter the year\n"))

if year % 4 == 0:
    if year % 400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    print("It is not a leap year")
