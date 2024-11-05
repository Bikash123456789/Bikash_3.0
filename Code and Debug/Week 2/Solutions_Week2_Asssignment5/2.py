"""
 Q2. Write a program to display the n terms of a harmonic series and their 
sum.
 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
 Lets suppose n=5.
 1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""

n = int(input("Enter a number: "))
i = 1
gsum = 0
while i <= n:
    gsum = gsum + 1 / i
    i += 1

print(gsum)
