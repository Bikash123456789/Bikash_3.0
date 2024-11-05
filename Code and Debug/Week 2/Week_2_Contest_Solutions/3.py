"""
Q3. Create a function named sumNum(), which takes 2 parameters as n1 
and n2. Calculate and return the sum of all the numbers divisible by and 2 
and 7 between n1 to n2. Also if the sum is 0, then return -1.
"""


def sumNum(n1, n2):
    i = n1
    end = n2
    sum = 0
    while i <= end:
        if i % 2 == 0 and i % 7 == 0:
            sum += i
        i += 1
    if sum == 0:
        return -1
    return sum


print(sumNum(1, 10))