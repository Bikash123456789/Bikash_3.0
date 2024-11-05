#  Q3. Write a Python function that takes two lists and returns True if they 
# have at least one common element.

def comparelist(l1,l2):
    for i in l1:
        if i in l2:
            return True
        

print(comparelist([1,2,3,4,5],[6,7,8,9,0]))