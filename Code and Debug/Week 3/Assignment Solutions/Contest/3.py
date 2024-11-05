# Q3. Write a function named armstrongRange which accepts 2 integers n1
# and n2. Print all the numbers from n1 to n2 which are armstrong numbers.

def lengthOfNum(n):
    count = 0
    while n!=0:
        count += 1
        n = n//10
    return count

def isArmstrong(n:int)->bool:
    original_num = n
    sum_of_digits_cube = 0
    power = lengthOfNum(n)
    while n!=0:
        last_digit = n%10
        sum_of_digits_cube += last_digit**power
        n = n//10
    if original_num == sum_of_digits_cube:
        return True
    else:
        return False

def armstrongRange(n1,n2):
    for i in range(n1,n2+1):
        if isArmstrong(i):
            print(i)

armstrongRange(56,1000)
# print(lengthOfNum(5647))