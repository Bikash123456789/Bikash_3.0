#  Q2. Write a function to remove duplicates from a list and print them.

list = [1,2,3,4,4,5,7,2,2,1,1,8,8,9,9,9,0,0,0]

def removeDuplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    
    return new_list

print(removeDuplicates(list))