"""
Write a program to remove the nth index element from a list using a function.
"""
lst = [1,2,3,4]
def removeNth(lst,n):
    lst.pop(n)

removeNth(lst,2)
print(lst)