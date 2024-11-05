list = [1,2,3,3,4,5,5,5,5,6,7,7,7,7,8,8,2,2,2,1,0,9,9,9,9]


def maxthree(list):
    new_list = []
    for num in list:
        if list.count(num) > 3:
            if num not in new_list:
                new_list.append(num)
    return new_list

print(maxthree(list))