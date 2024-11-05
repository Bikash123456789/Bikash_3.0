# Ask a number from user.
# If divisible by 3 print foo
# If divisible by 5 print bar
# If divisible by both 3 and 5 print foobar
# If not divisible by both 3 and 5 print foofoobarbar

num = int(input("Enter a number"))

if num % 3 == 0 and num % 5 == 0:
    print("foobar")
elif num % 5 == 0:
    print("bar")
elif num % 3 == 0:
    print("foo")
else:
    print("foofoobarbar")
