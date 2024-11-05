# Q5. Write a program to put all the common elements (in 2 lists) in another 
# list and print it using function.

def common(l1,l2):
    list = []
    for i in l1:
        if i in l2:
            list.append(i)
    return list

l1 = [34,11,91,59,33,22]
l2 = [78,14,23]

print(common(l1,l2))