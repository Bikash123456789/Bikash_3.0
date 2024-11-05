"""
Q7. Make two lists of same length and pass it to a function. Return a third 
list where each element is the sum of index
"""
l1 = [1,2,3,4]
l2 = [3,4,5,6]
def func(l1,l2):
    list = []
    for i in range(len(l1)):
        list.append(l1[i]+l2[i])
    return list

print(func(l1,l2))
