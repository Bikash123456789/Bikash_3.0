"""
 Q1. Make your own list of numbers. Ask a start and end position from User. 
Print the list from start position to end position using without using Slicing
"""

l = [1,2,3,3,4,5,6,76,8,10]

start = int(input("Enter a start point"))
end = int(input("Enter an end point"))

for i in range(start,end+1):
    print(l[i])