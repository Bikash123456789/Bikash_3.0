"""
Reverse a number
"""

n = int(input("Enter a number: "))
newnumber = 0
while n != 0:
    remainder = n % 10
    newnumber = newnumber * 10 + remainder
    n = n // 10

print(newnumber)
