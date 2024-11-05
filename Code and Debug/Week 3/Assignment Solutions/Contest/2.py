"""
Q2. Write a function named notPrimeNumbers which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are not prime.
"""

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def notPrimeNumbers(n1,n2):
    for i in range(n1,n2+1):
        if not(isPrime(i)):
            print(f"{i} is not a Prime Number")

        

notPrimeNumbers(2,20)