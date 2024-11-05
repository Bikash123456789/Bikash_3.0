# For integers, everything except zero is truthy and 0 is falsy
# For float, everything except 0.0 is truthy and 0.0 is falsy
# For string, everything except empty string is truthy and only "", '' is falsy

a = bool(5)
print(a)

b = bool(0)
print(b)

c = bool("Bikash")
print(c)

d = bool("")
print(d)
