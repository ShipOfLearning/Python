## @ShipOfLearning 
## List Method Append, Insert, Extend

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')  # Adds 'orange' to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.insert(0, 'kiwi')  # Inserts 'kiwi' at index 1
print(fruits)  # Output: ['kiwi', 'apple', 'banana', 'cherry', 'orange']
fruits.extend(['mango', 'grape'])  # Adds multiple items to the end of the list 
print(fruits)  # Output: ['kiwi', 'apple', 'banana', 'cherry', 'orange', 'mango', 'grape']