"""
Q1. Calculate the cube of all numbers from 1 to a given number.
"""

n = int(input("Enter a number : "))

for i in range(1,n+1):
    print(f"Cube of {i} is {i**3}")