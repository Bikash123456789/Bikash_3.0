#  Q1. Make a list of your own. Make two more empty list like odd and even. 
# Put all the even numbers from original list to even and odd numbers to 
# odd and print both lists. (Don’t remove anything from original one).

list = [1,2,3,4,5,6,7,8,9,10]

odd = []
even = []

for number in list:
    if number%2 == 0:
        even.append(number)
    else:
        odd.append(number)
    
print(even)
print(odd)