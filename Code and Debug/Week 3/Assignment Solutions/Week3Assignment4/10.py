"""
 Q10. Ask 10 numbers from the user and put them into the list. Now remove 
all the even numbers from that list.
"""

list = []
for i in range(10):
    n = int(input(f"Enter number {i+1} : "))
    list.append(n)

for i in list:
    if i%2 == 0:
        list.remove(i)
    
print(list)
