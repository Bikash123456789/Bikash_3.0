# Find the sum of all numbers between start and end

start = int(input("Enter the start :"))
end = int(input("Enter the end :"))

i = start
sum = 0
while i <= end:
    sum = sum + i
    i = i + 1

print(sum)
