# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print("a is b:", a is b)  # True, both refer to the same object
# print("a is c:", a is c)  # False, different objects with same content

# print("Memory location of a:", id(a))
# print("Memory location of b:", id(b))
# print("Memory location of c:", id(c))

# Membership operator demonstration

# List
numbers = [10, 20, 30]
print(20 in numbers)        # True
print(40 not in numbers)    # True

# String
text = "Python"
print("P" in text)          # True
print("z" not in text)      # True
print("P" not in text)      # false

# Dictionary (checks keys)
info = {"name": "Alice", "age": 25}
print("name" in info)       # True
print("Alice" in info)      # False

# Tuple
values = (1, 2, 3)
print(2 in values)          # True
print(4 not in values)      # True