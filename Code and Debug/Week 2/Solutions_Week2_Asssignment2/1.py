def largest(a=None, b=None, c=None) -> int:
    if a == None or b == None or c == None:
        return -1

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


returnedValue = largest(4.8, 5.89)
if returnedValue == -1:
    print("Enter valid numbers")
else:
    print(f"The largest number is {returnedValue}")
