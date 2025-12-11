# ============================================
# FUNCTION DEFINITION AND USAGE DEMONSTRATION
# ============================================

# 1. BASIC FUNCTION DEFINITION
# Syntax: def function_name(parameters):
#             code block
#             return value (optional)

def greet():
    print("Hello, Welcome to Python!")

# Call the function
greet()


# 2. FUNCTION WITH PARAMETERS
# Parameters are variables that function accepts

def add(num1, num2):
    """Function that adds two numbers"""
    result = num1 + num2
    # print(f"Adding {num1} and {num2} gives {result}")
    return result

# Call the function with arguments
# add(5, 10)
sum_result = add(5, 10)
print(f"Sum: {sum_result}")


# 3. FUNCTION WITH MULTIPLE PARAMETERS AND RETURN

def calculate_area(length, width):
    """Function to calculate rectangle area"""
    area = length * width
    return area

# Call and use the returned value
rect_area = calculate_area(5, 8)
print(f"Rectangle Area: {rect_area}")
print(f"Rectangle Area: {calculate_area(5, 8)}")

def calculate_expo(number, y=2):
    """Function to calculate square of a number"""
    squere = number ** y
    return squere

print(f"Squere of 5 is: {calculate_expo(5)}")
print(f"Cube of 5 is: {calculate_expo(5,3)}")

# 4. FUNCTION WITH DEFAULT PARAMETERS

def introduce(name, age=25):
    """Function with default parameter value"""
    print(f"Name: {name}, Age: {age}")

introduce("Alice")  # Uses default age
introduce("Bob", 30)  # Overrides default age


# 5. FUNCTION WITH MULTIPLE RETURN VALUES

def get_name_and_age():
    """Function returning multiple values"""
    return "John", 28

name, age = get_name_and_age()
print(f"{name} is {age} years old")

def add_sub_mul_div(a, b):
    """Function to perform multiple arithmetic operations"""
    print(f"Values received: a={a}, b={b}")
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division

add, sub, mul, div = add_sub_mul_div(2,10)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

add, sub, mul, div = add_sub_mul_div(b=10,a=5)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
# 6. FUNCTION WITH *args (Variable Number of Arguments)

def add_numbers(*args):
    """Function that accepts any number of arguments and returns their sum"""
    total = 0
    for num in args:
        total += num
    return total

# Example 1: Add 2 numbers
result1 = add_numbers(5, 10)
print(f"Sum of 5 and 10: {result1}")

# Example 2: Add 5 numbers
result2 = add_numbers(1, 2, 3, 4, 5)
print(f"Sum of 1, 2, 3, 4, 5: {result2}")

# Example 3: Take input from user
print("\nEnter numbers separated by space:")
user_input = input("Enter numbers: ")
numbers = list(map(int, user_input.split()))
result3 = add_numbers(*numbers)
print(f"Sum of entered numbers: {result3}")

# 7. FUNCTION WITH **kwargs (Variable Number of Keyword Arguments)

def print_info(**kwargs):
    """Function that accepts any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example 1: Print person information
print_info(name="Alice", age=25, city="New York")

# Example 2: Print product details
print_info(product="Laptop", price=999, brand="Dell", color="Silver")

# Example 3: Combine *args and **kwargs
def describe_person(*args, **kwargs):
    """Function with both args and kwargs"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

describe_person("John", 28, name="John", age=28, city="Boston")