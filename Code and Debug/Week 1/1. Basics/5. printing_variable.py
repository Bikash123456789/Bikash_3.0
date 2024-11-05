name = "Bikash"
age = 27
gender = "Male"

print(name, age, gender)

print("Method 1 - ")
print("My name is", name)
print("My age is", age)
print("My gender is", gender)
print("My name is", name, "my age is", age, "my gender is", gender)
print("---------------")

print("Method 2 -  F-strings")
print(f"My name is {name}")
print(f"My age is {age}")
print(f"My gender is {gender}")
print(f"My name is {name}, my age is {age} and my gender is {gender}")

print("------------------")
print("Method 2 - used for debugging")
print(f"{name=}")
