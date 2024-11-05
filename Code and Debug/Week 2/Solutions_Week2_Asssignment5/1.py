"""
Q1. 2  22  222  2222  22222 ... upto n. (Ask n from user)
"""

n = int(input("Enter a number: "))

i = 1
num = 0
while i <= n:
    num = num * 10 + 2
    print(num, end=" ")

    i += 1
