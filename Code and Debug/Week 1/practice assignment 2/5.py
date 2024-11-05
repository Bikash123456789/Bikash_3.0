billamt = int(input("Enter your bill amout\n"))

discount = 0

if billamt > 50000:
    discount = 30 * billamt / 100
elif 40000 <= billamt <= 49999:
    discount = 25 * billamt / 100
elif 30000 <= billamt <= 39999:
    discount = 20 * billamt / 100
elif 10000 <= billamt <= 29999:
    discount = 10 * billamt / 100
else:
    discount = 0

print("Discount :", discount)
print("Total Bill :", billamt - discount)
