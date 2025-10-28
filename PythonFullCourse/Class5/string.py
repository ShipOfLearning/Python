## Reversing a String in Python
str1 = "KiranKumar"
print(str1[::-1])  # Reversed string

## Slicing in Python Strings
# string[start:end:step]
str1 = "KiranKumar"
# print(str1[0:5])    # Kiran
# print(str1[5:10])   # Kumar
# print(str1[:5])     # Kiran
# print(str1[5:])     # Kumar

## Steps in Slicing
# print(str1[::2])   # Kranua
print(str1[::3])

## Indexing in Python Strings
str1 = "KiranKumar"
# K i  r  a  n  K  u  m  a  r
# 0 1  2  3  4  5  6  7  8  9
#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(str1[0])    # K
print(str1[4])    # n

## String Operations in Python
a = "Python"
b = "Programming"
print(a + " " + b)  # Concatenation
print(a * 3)        # Repetition
print("Py" in a)  # Membership
print("Java" in a)  # Membership



## Different ways to declare string in python
str1 = 'KiranKumar\'s'
str2 = "KiranKumar Roy.\n\tToday is very \"beautiful\" day"
str3 = ''' My name is KiranKumar 
and we are learning python programming. my laptop's battry is draining fast.
today is very "beautiful" day''' #Multi-line string

print(str1)
print(str2) 
print(str3)

## Demonstrating various string methods in Python

str1 = "Hello, World World!"
str2 = "pythonprogramming"
str3 = "12345"

print("Original:", str1,str2,str3)
print("strip():", str1.strip())  # Removes whitespace from both ends
print("lower():", str1.lower())  # Converts to lowercase
print("upper():", str1.upper())  # Converts to uppercase
print("replace():", str1.replace("World", "Python"))  # Replace substring
print("split():", str1.split(" "))  # Split into list
print("find():", str1.find("X"))  # Find substring index
print("count():", str1.count("X"))  # Count occurrences
print("startswith():", str1.startswith("He"))  # Check start
print("endswith():", str1.endswith("!"))  # Check end
print("capitalize():", str2.capitalize())  # Capitalize first letter
print("title():", str2.title())  # Title case
print("isdigit():", str3.isdigit())  # Check if all digits
print("isalpha():", str2.isalpha())  # Check if all alphabetic (will be False due to space)
print("join():", "-".join(["2025", "10", "28"]))  # Join list with separator

