def sumCountOddEven(list):
    sumEven = 0
    sumOdd = 0
    for ele in list:
        if ele % 2 == 0:
            sumEven += ele
        else:
            sumOdd += ele
    print(f"The even numbers sum is {sumEven} and the odd numbers sum is {sumOdd}")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
sumCountOddEven(a)
