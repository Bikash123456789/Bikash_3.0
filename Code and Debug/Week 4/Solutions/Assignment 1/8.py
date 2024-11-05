"""
Q8. Write a Python code to split a list into two halves using list slicing. 
(Keep the length of list even).
"""

list = [1,2,3,4,5,6]

l1 = list[:len(list)//2]
l2 = list[len(list)//2:]

print(l1)
print(l2)