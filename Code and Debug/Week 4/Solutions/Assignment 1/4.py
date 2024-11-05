"""
 Q4. Make your own list. Write a Python program that takes an integer as an 
input, and make a new list containing the last n elements of the original 
list. Using slicing logic.
"""

list = [1,2,3,4,5]

n = int(input("Enter a number"))

print(list[-n:])