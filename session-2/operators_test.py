# Operators Test
#
# Short Test script to demonstrate arithmetic, logical, and unary operators
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-14
#

x = 15
y = 20
print("x =", x, "\n" + "y =", y)

# Arithmetic Operators
print("Arithmetic Operators \n")

print("x + y =", x + y, "(Addition (+) )")
print("x - y =", x - y, "(Subtraction (-) )")
print("x * y =", x * y, "(Multiplication (*) )")
print("x ** y =", x ** y, "(Power (**) )")
print("y / x =", y / x, "(Division (/) )")
print("y % x =", y % x, "(Modulo (Remainder) (%) )")

print("\n")

# Logical Operators
print("Logical Operators \n")

print("x == y", x == y, "(Equal To (==) )")
print("x != y", x != y, "(Not Equal To (!=) )")
print("x < y", x < y, "(Less Than (<) )")
print("x <= y", x <= y, "(Less Than/Equal To (<=) )")
print("x > y", x > y, "(Greater Than (>) )")
print("x >= y", x >= y, "(Greater Than/Equal To (>=) )")

print("\n")

# Unary Operators
print("Unary Operators \n")

print("Add to self (+=):")
print("x =", x)
print("x += 1")
x += 1
print("x =", x, "\n")

print("Subtract from self (-=):")
print("x =", x)
print("x -= 1")
x -= 1
print("x =", x, "\n")
