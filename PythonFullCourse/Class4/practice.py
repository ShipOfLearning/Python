#  Write a program to compute simple interest: "SI = (P × R × T) / 100"
principle = 100
rate = 3
tenure = 12
SI = (principle * rate * tenure)/100
print(f"the simple interest of given value is {SI}")

#  Find the last digit of any number 
num1 = int(input("Enter any number : "))
print(f"the last digit of given number is {num1 % 10}")

#  Find the square of the sum of two numbers.
num1 = 1
num2 = 3
result = num1 + num2
print(f"the square of restul is {result ** 2}") 

#  Convert Celsius to Fahrenheit: "C = 37" → "F = (C * 9/5) + 32" 
c = 37
f = (c * 9/5) + 32
print(f"the fahrenheit is {f} of {c} celsius")

#  Compute area of a rectangle: length = 12, width = 5
length = 12
width = 5
print(f"the area of given dia is {length * width}")

#  Find the cube of a number using "**"
num1 = 2
print(f"the cube of given number is {num1 ** 3}")

#  Find average of three numbers: 15, 27, 33
num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))
num3 = int(input("Enter the third Number : "))
print(f"the average of given number is {(num1 + num2 + num3)/3}")

#  Calculate total cost: price = 499, quantity = 3 
price = 499
quantity = 3
print(f"the total price of item is {price * quantity}")

#  Calculate "a = 2" raised to the power "b = 4" 
a = 2
b = 4
print(f"the result is {a**b}")

#  Find the remainder of "a = 28" by "b = 6"
a = 28
b = 6
print(f"the reuslt is {a % b}")

#  Find the floor division result of "a = 17" and "b = 4" 
a = 17
b = 4
print(f"the reuslt is {a//b}")

#  Divide "a = 25" by "b = 5" (use "/") 
a = 25
b = 5
print(f"the reusult is {a / b}")

# Multiply "a = 7" with "b = 9" 
a = 7
b = 9
print(f"the reusult is {a * b}")

# Subtract "b = 5" from "a = 20"
a = 20
b = 5
print(f"the result is {a - b}")

# Add two numbers: "a = 12", "b = 8" 
a = 12
b = 8
print(f"the result is {a * b}")

#  Store two float numbers and print their multiplication. 
num1 = 12.5
num2 = 6.3
print(f"the result is {num1 * num2}")

# Use variables to form a sentence like "My name is KK and I am 25 years old.“ and print it
name = input("enter the Name : ") 
age = int(input("enter the Age : "))
print(f"My name is {name} and I am {age} years old.")

#  Store a boolean value and print it.
var1 = False
print(f"the value of var1 is {var1}")

# Convert a string "123" to an integer and add 1. 
var1 = "123"
result = int(var1) + 1
print(f"the result is {result}")

#  Convert an integer variable to float and print.
num1 = 12
print(f"the converted value of num1 is {float(num1)}")

# Swap the values of two variables and print the result. 
num1 = 12
num2 = 6
print(f"the value of num1 and num2 is {num1} and {num2}")
# Method 1
num1, num2 = num2, num1
# # Method 2
# temp = num1
# num1 = num2
# num2 = temp
print(f"the value of num1 and num2 after swapping is {num1} and {num2}")

# Store different types of data in variables and print their types. 
var1 = "kirankumar"
var2 = 12
var3 = 12.5
var4 = [1,2,3]
var5 = (1,21.3)

print(f"the type of vaiable var1 is {type(var1)}")
print(f"the type of vaiable var2 is {type(var2)}")
print(f"the type of vaiable var3 is {type(var3)}")
print(f"the type of vaiable var4 is {type(var4)}")
print(f"the type of vaiable var5 is {type(var5)}")

# Combine two strings (like first and last name) and print the result. 
first_name = "KiranKumar"
last_name = "Roy"
print(f"{first_name} {last_name}")

# Store two numbers in variables and print their sum.
num1 = 15
num2 = 20
result = num1 + num2

print(f"the sum of num1 and num2 is {num1 + num2}")
print(f"the result of num1 and num2 {result}")

# Store your name in a variable and print it. 
name = "KiranKumar Roy"
print(f"My name is {name}")
