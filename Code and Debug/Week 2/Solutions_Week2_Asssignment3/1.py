def div(num1, num2):
    i = num1
    end = num2
    while i <= end:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
        i = i + 1


div(1, 60)
