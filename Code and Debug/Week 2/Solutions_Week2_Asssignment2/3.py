def middleNumber(a, b, c):
    if a < b < c:
        return b
    elif b < a < c:
        return a
    else:
        return c


middlenum = middleNumber(12, 2, 18)
print(f"Middle num is {middlenum}")


def div(num):
    if num % 4 == 0 and num % 3 == 0:
        return True
    else:
        return False


print(div(middlenum))
