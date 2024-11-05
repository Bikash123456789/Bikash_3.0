"""
 Q2. Write a Python program to generate a list of factorials less than 1000 
using list comprehension.
 Example output: [1, 2, 6, 24, 120, 720]
"""

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(5))

a = [factorial(i) for i in range(1,100) if factorial(i) < 1000]

print(a)