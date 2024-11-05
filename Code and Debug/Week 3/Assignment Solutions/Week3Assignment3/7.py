import sys


def findLargest(list):
    largest = -sys.maxsize - 1
    for ele in list:
        if ele >= largest:
            largest = ele
    return largest


a = [34, 11, 91, 59, 33, 22]
x = findLargest(a)
print(x)
