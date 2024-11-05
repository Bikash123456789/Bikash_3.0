def printNumber(n: int) -> str:
    if n == 1:
        return "One"
    elif n == 2:
        return "Two"
    elif n == 3:
        return "Three"
    elif n == 4:
        return "Four"
    elif n == 5:
        return "Five"
    elif n == 6:
        return "Six"
    elif n == 7:
        return "Seven"
    elif n == 8:
        return "Eight"
    elif n == 9:
        return "Nine"
    else:
        return "Zero"


def reverseNumber(n):
    reversedNumber = 0
    while n > 0:
        remainder = n % 10
        reversedNumber = reversedNumber * 10 + remainder
        n = n // 10
    return reversedNumber


def printWords(n: int):
    n = reverseNumber(n)
    while n > 0:
        remainder = n % 10
        value = printNumber(remainder)
        print(value, end=" ")
        n = n // 10


printWords(456900)
