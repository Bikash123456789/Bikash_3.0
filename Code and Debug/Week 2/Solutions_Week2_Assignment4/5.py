"""
 Q6. Don’t create a function, just print the following pattern
 1  11  111  1111  11111....n times (Ask n from user
"""

n = int(input("Enter a number: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("1", end="")
        j = j + 1
    print(end=" ")
    i += 1
