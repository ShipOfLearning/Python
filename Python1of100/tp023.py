## @ShipOfLearning
## List Methods - remove, pop, clear


fruits = ["banana", "apple", "cherry", "kiwi", "mango"]
fruits.remove("apple")  # Removes "apple" from the list
print(fruits)  # Output: ['banana', 'cherry', 'kiwi', 'mango']
fruits.pop(2)  # Removes the item at index 2 ("kiwi")
print(fruits)  # Output: ['banana', 'cherry', 'mango']
str = fruits.pop()
print(fruits)  # Removes the last item ("mango"), Output: ['banana', 'cherry']
print(str)  # Output: mango
fruits.clear()  # Removes all items from the list
print(fruits)  # Output: []
print(id(fruits))  # Output: 0
fruits = []
print(id(fruits))  # Output: 0