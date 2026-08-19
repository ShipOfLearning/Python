## @ShipOfLearning
## List Methods - sort vs sorted

num1 = [5, 2, 9, 1, 5, 6]
num2 = [3, 4, 1, 2, 5]

num1.sort()  # This will sort num1 in place
print("Sorted num1:", num1)  # Output: Sorted num1: [1

num3 = sorted(num2)  # This will return a new sorted list from num2
print("Sorted num3:", num3)  # Output: Sorted num2: [1, 2, 3, 4, 5]
print("Original num2:", num2)  # Output: Original num2: [3, 4, 1, 2, 5]