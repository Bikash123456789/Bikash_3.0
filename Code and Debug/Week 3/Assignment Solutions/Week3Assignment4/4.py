# Q4. Write a Python Program to find sum and average of List in Python.

list = [1,2,3,4,5,6,7,8,9,10]

sum = 0
average = 0
for i in list:
    sum = sum + i

print(f"Sum : {sum}")
print(f"Average : {sum/len(list)}")