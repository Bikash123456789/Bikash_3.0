"""
What is Statically typed language and Dynamic Type Language
"""

"""
You have to do a small change for more strict variable declaration.
1. Ctrl + Shift + P
2. Type Open Workspace settings json
3. Paste {
    "python.analysis.typeCheckingMode": "basic"
} in that file and save it
"""

a: int = (
    5  # this is to inform to store integer in a but it can store any other datatype.
)
print(a)

# a = "Bikash"
# print(a)


b: int | float = 55
