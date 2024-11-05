def reverseNumber(n):
    reversedNumber = 0
    while n > 0:
        remainder = n % 10
        reversedNumber = reversedNumber * 10 + remainder
        n = n // 10
    return reversedNumber


def checkPalindrome(n):
    if n == reverseNumber(n):
        print(True)
    else:
        print(False)


checkPalindrome(23)
