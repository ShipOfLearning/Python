# Demonstrating different datatypes in Python

# Without casting (input returns string, so concatenation happens)
a = input("Enter first value: ")
b = input("Enter second value: ")
print("Result without casting:", a + b)

# With casting (convert input to integer before addition)
a_int = int(input("Enter first integer: "))
b_int = int(input("Enter second integer: "))
print("Result with casting:", a_int + b_int)

user_input = input("Enter any value: ")
print(f"Value entered: {user_input}")
print(f"Type of value: {type(user_input)}")

# Integer
age = 25
print(f"the type of variable age is {type(age)}")

# Float
height = 5.9
print(f"the type of variable height is {type(height)}")

# String
name = "Alice"
print(f"the type of variable name is {type(name)}")

# Boolean
is_student = True
print(f"the type of variable is_student is {type(is_student)}")


# List
fruits = ["apple", "banana", "cherry"]
print(f"the type of variable fruits is {type(fruits)}")

# Tuple
coordinates = (10.5, 20.3)
print(f"the type of variable coordinates is {type(coordinates)}")

# Dictionary
person = {"name": "Bob", "age": 30}
print(f"the type of variable person is {type(person)}")

# Set
unique_numbers = {1, 2, 3, 4}
print(f"the type of variable unique_numbers is {type(unique_numbers)}")

# NoneType
nothing = None
print(f"the type of variable nothing is {type(nothing)}")