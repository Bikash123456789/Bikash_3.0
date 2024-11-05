 #  Pass by value
def change(a: int):
    a = 1000
a = 50
change(a)
print(a)





#  Pass by reference
def display(lst):
    lst[0] = 100
    print(lst)


my_list = [45, 34, 45, 56, 67]
display(my_list)
print(my_list)
