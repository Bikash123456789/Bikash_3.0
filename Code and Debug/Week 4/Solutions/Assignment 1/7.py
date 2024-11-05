"""
 Q7. Write a python program to interchange first and last elements in a list.
"""

list = [1,2,3,4,5]

list[0],list[-1] = list[-1],list[0]

print(list)