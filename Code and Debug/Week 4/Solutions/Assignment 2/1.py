"""
 Q1. Write a Python program to generate a list of powers of 2 less than 100 
using list comprehension.
 Example output: [1, 2, 4, 8, 16, 32, 64]
"""

a = [2**i for i in range(10) if 2**i < 100]
print(a)