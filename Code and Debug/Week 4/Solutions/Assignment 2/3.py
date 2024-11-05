"""
 Q3. Write a Python program to generate a list of prime numbers less than 
500 using list comprehension.
 Example output: [2, 3, 5, 7, 11, 13, 17, 19, 23, ..., 491, 499]
 500 can be changed to anything.
"""

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

a = [i for i in range(1,500) if isPrime(i)==True]
print(a)