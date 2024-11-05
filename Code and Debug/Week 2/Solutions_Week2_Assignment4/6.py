"""
 Q7. Keep asking numbers from user until the user enters 0. Then display 
the average of all numbers.
"""

sum = 0
count = 0
while True:

    n = int(input("Enter a number: "))
    if n == 0:
        break
    sum = sum + n
    count += 1

print(f"{sum/count}")
