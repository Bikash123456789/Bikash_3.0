"""
Q5. Count how many numbers are divisible by 3 and 6 between 1 to 1000 
by using list comprehension
"""

a = [i for i in range(1,1000) if (i%3 == 0 and i%6 == 0)]
print(a)
print(len(a))