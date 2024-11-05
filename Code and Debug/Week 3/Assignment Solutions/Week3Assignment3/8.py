import sys


def findSmallest(list):
    smallest = sys.maxsize
    for ele in list:
        if ele <= smallest:
            smallest = ele
    return smallest


a = [34, 11, 91, 59, 33, 22]
x = findSmallest(a)
print(x)
