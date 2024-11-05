def updateOddEven(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list[i] = list[i] + 1
        else:
            list[i] = list[i] - 1


a = [34, 11, 91, 59, 33, 22]
updateOddEven(a)
print(a)
