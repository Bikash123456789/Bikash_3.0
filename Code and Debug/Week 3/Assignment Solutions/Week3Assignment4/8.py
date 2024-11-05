"""
Q8. Take 10 integer inputs from user and store them in a list. Now, copy all 
the elements in another list but in reverse order
"""
list = []
for i in range(10):
    n = int(input(f"Enter number {i+1} : "))
    list.append(n)

print(list)


new_list = []
for i in range(len(list)):
    new_list.append(list[-(i+1)])

print(new_list)