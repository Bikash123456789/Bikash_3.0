"""
Q4. Write a Python program to check if a triangle is equilateral, isosceles or
scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides
"""

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a==b and b==c and c==a:
    print("Equilateral")
elif (a==b) or (b==c) or (c==a):
    print("Isosceles")
else:
    print("Scalene")