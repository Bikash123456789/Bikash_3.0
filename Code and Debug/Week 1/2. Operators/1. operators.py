"""
Operators

1. Arithmetic
2. Assignment
3. Comparision
4. Logical
5. Membership
6. Identity
7. Bitwise
"""

"""
Arithmetic
+
- 
/ (Float)
*
%
**
// (Floor Division) (Always in INT) (Lowest Integer)
"""

a = -16
b = 5

print(a / b)
print(a // b)
# print(a % b)
# print(a**b)  # a^b = 10^5 =10*10*10*10*10
# print(a + b)
# print(a - b)
# print(a / b)
# print(a * b)


"""
Assignment Operator
To as sign a value
+=
-=
*=, /=, //=, **=
"""

a = 5
# a = a + 3
# a += 3
# a *= 3  # a = a*3 = 5*3 = 15
a **= 3
print(a)


"""
Comparision (always comes in bool)
>
< 
>=
<=
==
!=
"""

a = 20
b = 15
c = 20
# print(a < b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
print(a == b == c == a)


"""
Logical Operators (To compare 2 or more conditions) (Always in BOOL)
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (reverses the result)
"""

physics = 16
chemistry = 20
maths = 66
print(physics > 33 and chemistry > 33 and maths > 33)
# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)
# print(not (physics > 33 or chemistry > 33))
print(physics > 33 and not chemistry > 33)
# F and T -> F
print(not physics > 33)
