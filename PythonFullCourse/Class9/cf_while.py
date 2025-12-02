numbers = [1, 2, 3, 4, 5]
squares = []
index = 0

while index < len(numbers):
    # pass
    if index == 3:
        # break # Exit loop when index is 3
        continue # Skip the iteration when index is 3
    squares.append(numbers[index] ** 2)
    print("Current index:", index)
    index += 1
else:
    print("Completed squaring all numbers.")

print("Original numbers:", numbers)
print("Squares:", squares)