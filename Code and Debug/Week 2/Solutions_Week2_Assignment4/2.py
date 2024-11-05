"""
 Q2. From 1 to 2000, print all the LEAP YEARS, using WHILE loop.
"""


def isLeap(n: int) -> int:
    if n % 4 == 0 or n % 400 == 0:
        if n % 100 != 0:
            return True
        else:
            return False
    else:
        return False


def countLeapYears():
    i = 1
    while i <= 2000:
        if isLeap(i):
            print(i, end=" ")
        i = i + 1


countLeapYears()
