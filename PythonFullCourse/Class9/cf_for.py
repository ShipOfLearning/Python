# Define a list of integers
numbers = [1, 2, 3, 4, 5]

# Iterate through the list using a for loop
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("Finished iterating through the list.")


base = 9
for i in range(1, 11):
    print(f"{base} x {i} = {base * i}")

base = 9
for i in range(1, 11,2):
    print(f"{base} x {i} = {base * i}")

base = 9
for i in range(2, 12,2):
    print(f"{base} x {i} = {base * i}")
    
# Define a list of integers
numbers = [10, 20, 30, 40, 50]

# Iterate through the list using a for loop
for num in numbers:
    print(num)