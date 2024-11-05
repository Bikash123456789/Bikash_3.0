totalclasses = int(input("Enter the total number of classes"))
attendedclasses = int(input("Enter the total number of attended classes"))

attendancepercent = (attendedclasses / totalclasses) * 100

print(attendancepercent)

if attendancepercent >= 75:
    print("Allowed to sit")
else:
    print("Not allowed to sit")
