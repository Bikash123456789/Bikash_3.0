n = 7
n1 = n//2 + 1
n2 = n//2


for i in range(1,n1+1):
    for j in range(1,i):
        print(" ",end="")
    
    for j in range(1,n1-i+2):
        print("*", end=" ")
    
    print()

for i in range(1,n2+1):
    for j in range(1,n2-i+1):
        print(" ",end="")
    for j in range(1,i+2):
        print("*",end=" ")
    
    print()
