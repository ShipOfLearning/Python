numbers = [1, 2, 3]

new_numbers = numbers
new_numbers.append(4)
print(numbers)   
print(f"ID of numbers: {id(numbers)}")
print(f"ID of new_numbers: {id(new_numbers)}")

#Reason: Both variables point to the same list object in memory, so changes via one variable affect the other.
#explanation: The append method modifies the list in place, and since both variables reference the same list, the change is reflected in both.
#Output: [1, 2, 3, 4]