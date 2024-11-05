# Escape Sequence ( always comes in "")
"""

\n -> New Line
\t -> Tab
\\=> \
\" -> "
\' -> '
\b -> Backspace

"""

print("Hello World\nGood Bye\nWe are learning python")
print("-------------------------------------")
print("Hello World\tGood Bye\tWe are learning python")
print("-------------------------------------")
print("Hello World\tGood Bye\n\n\nWe are learning python")
print("-------------------------------------")


# output1:- My name is B\ikash
print("My name is B\\ikash")
print("-------------------------------------")

# output2:- My name is "Bikash"
print('My name is "Bikash"')
print("-------------------------------------")

# output2:- a"\\"xyz'"\
print('a"\\\\"xyz\'"\\')
print("-------------------------------------")
