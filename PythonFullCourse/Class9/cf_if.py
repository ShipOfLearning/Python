# Demonstrate if-else statements in Python

# Example 1: Simple if-else
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: if-elif-else
score = int(input("Enter your test score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Example 3: Nested if-else
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Example: Ternary (conditional) expression examples

# 1) Determine parity with a single-line ternary print
n = int(input("Enter an integer: "))
print("Even" if n % 2 == 0 else "Odd")

# 2) Use ternary to pick the larger of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
larger = a if a > b else b
print(f"Larger number: {larger}")

# Example: Using logical operators (and, or, not) in if-elif-else

username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

# Using 'and' operator - both conditions must be true
if username == "admin" and password == "1234":
    print("Login successful!")
elif username == "admin" and password != "1234":
    print("Incorrect password!")
# Using 'or' operator - at least one condition must be true
elif age >= 18 or username == "guest":
    print("Access granted!")
# Using 'not' operator - negates the condition
elif not (username == "admin" or username == "guest"):
    print("Unknown user!")
else:
    print("Access denied!")