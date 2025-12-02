# A dictionary in Python is an unordered collection of key:value pairs,
# where each key is unique and used to access its corresponding value.

# One student object represented as a dictionary
student = {
    "id": 101,
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["CS101", "MATH200"]
}

# Print the student dictionary
print(f"Original Student : {student}")

# # Most used dict methods:
# keys, values, items
# print("Keys:", list(student.keys()))
# print("Values:", list(student.values()))
# print("Items:", list(student.items()))

# # get (with default)
# print("GPA (get):", student.get("gpa"))
# print("Nickname (get with default):", student.get("nickname", "No nickname"))

# # setdefault (adds key if missing)
# email = student.setdefault("email", "alice@example.com")
# print("Email set with setdefault:", email)
# print("Student after setdefault:", student)

# # update (merge another dict)
# student.update({"age": 21, "gpa": 3.9})
# print("After update - age:", student)

# # pop (remove by key)
# removed_major = student.pop("major", "No major")
# print("Popped major:", removed_major)
# print("Student after pop:", student)

# # popitem (remove and return last inserted key-value)
# last_item = student.popitem()
# print("Popitem removed:", last_item)
# print("Student after popitem:", student)

# # copy (shallow copy)
# student_copy = student.copy()
# student_copy["name"] = "Bob"
# print("Original name:", student["name"], "| Copy name:", student_copy["name"])

# # clear (empties a dict)
# temp_dict = {"a": 1, "b": 2}
# temp_dict.clear()
# print("Temp after clear:", temp_dict)

# # fromkeys (class method to create a dict)
# defaults = dict.fromkeys(["x", "y"], "default_value")
# print("fromkeys result:", defaults)

# Differences between List, Tuple, Set, and Dictionary

# | Feature         | List                   | Tuple                  | Set                     | Dictionary               |
# |------------------|-----------------------|------------------------|-------------------------|--------------------------|
# | Definition       | Ordered collection     | Ordered immutable      | Unordered collection     | Unordered key-value pairs |
# | Syntax           | [1, 2, 3]             | (1, 2, 3)              | {1, 2, 3}               | {"key": "value"}        |
# | Mutability       | Mutable               | Immutable              | Mutable                 | Mutable                  |
# | Duplicates       | Allows duplicates      | Allows duplicates      | No duplicates            | Keys must be unique      |
# | Access           | Indexed access         | Indexed access          | No indexing              | Key-based access         |
# | Use Cases        | Ordered data           | Fixed data             | Unique items             | Key-value associations    |
