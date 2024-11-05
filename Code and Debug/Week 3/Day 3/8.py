a = [78, 67, 44, 100, 87, 33, 31]

eventotal = 0

for ele in a:
    if ele % 2 == 0:
        eventotal += ele

print(eventotal)


evenPositionTotal = 0
for i in range(0, len(a)):
    if i % 2 == 0:
        evenPositionTotal += a[i]

print(evenPositionTotal)
