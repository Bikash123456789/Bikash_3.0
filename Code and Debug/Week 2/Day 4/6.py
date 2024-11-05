# Sum of digits

n = int(input("Enter a number: "))
sum = 0
while n != 0:
    right_most_digit = n % 10
    sum = sum + right_most_digit
    n = n // 10

print(sum)
