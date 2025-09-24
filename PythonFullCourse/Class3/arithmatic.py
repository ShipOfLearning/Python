# Demonstration of arithmetic operators in Python

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a + b}")        # Addition
print(f"{a} - {b} = {a - b}")        # Subtraction
print(f"{a} * {b} = {a * b}")        # Multiplication
print(f"{a} / {b} = {a / b}")        # Division
print(f"{a} % {b} = {a % b}")        # Modulus
print(f"{a} ** {b} = {a ** b}")      # Exponentiation
print(f"{a} // {b} = {a // b}")      # Floor Division

if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

