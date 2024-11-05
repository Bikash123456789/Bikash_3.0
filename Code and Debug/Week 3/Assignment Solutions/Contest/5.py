n = 5

for i in range(1,n+1):
    # spaces
    for j in range(1,i):
        print(" ",end=" ")

    # stars
    for j in range(1,2*(n-i)+2):
        print("*",end=" ")

    print()