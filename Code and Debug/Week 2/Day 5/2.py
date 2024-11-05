# 1 11 101 1001 10001
# i = 1
# val = 1
# number = 1
# while i <= 5:
#     print(number, end=" ")
#     val = val * 10
#     number = val + 1
#     i += 1

i = 1

val = 1
while i <= 5:
    print(val, end=" ")
    val = 10**i + 1

    i += 1
