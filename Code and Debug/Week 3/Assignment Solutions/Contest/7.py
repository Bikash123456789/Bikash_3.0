n = 4

for i in range(1,n+1):
    # Spaces
    for j in range(1,i):
        print(" ",end="")

    # Stars
    for j in range(1,n+1):
        print("*",end=" ")
    
    print()