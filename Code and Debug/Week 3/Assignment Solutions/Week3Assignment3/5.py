def countOddEven(list):
    even = 0
    odd = 0
    for ele in list:
        if ele % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"The list has {even} even numbers and {odd} odd numbers")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
countOddEven(a)
