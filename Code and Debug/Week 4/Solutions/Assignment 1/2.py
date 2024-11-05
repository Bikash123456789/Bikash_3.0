"""
 Q2. Make your own list of numbers. Ask a start and end position from User. 
Make another di erent list which will contain number from start to end 
position. Use slicing logic.
"""

list = [2,3,4,5,6,7]


start = int(input("Enter a start point"))
end = int(input("Enter an end point"))

new_list = list[start:end+1]
print(new_list)