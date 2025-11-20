# Most used methods of set in Python

# 1. add() - adds a single element to a set
my_set = {11,10,9,1, 2, 3,2,4,5}
my_set.add(4)
print(f"After add: {my_set}")

# 2. remove() - removes an element (raises KeyError if not found)
my_set.remove(2)
print(f"After remove: {my_set}")

# 3. discard() - removes an element (no error if not found)
my_set.discard(50)
print(f"After discard: {my_set}")

# 4. pop() - removes and returns an arbitrary element
popped = my_set.pop()
print(f"Popped: {popped}, Set: {my_set}")

# 5. clear() - removes all elements from the set
test_set = {1, 2, 3}
test_set.clear()
print(f"After clear: {test_set}")

# 6. union() - combines two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Union: {union_set}")

# 7. intersection() - returns common elements
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# 8. difference() - returns elements in first set but not in second
diff_set = set1.difference(set2)
print(f"Difference: {diff_set}")

# 9. copy() - creates a shallow copy of the set
copied_set = set1.copy()
print(f"Copied: {copied_set}")

# 10. issubset() - checks if set is a subset
subset_check = {1, 2, 4}.issubset({1, 2, 3})
print(f"Is subset: {subset_check}")

# 11. issuperset() - checks if set is a superset
superset_check = {1, 2, 3}.issuperset({1, 2})
print(f"Is superset: {superset_check}")

# A set is an unordered collection of unique, immutable elements in Python.
# Sets are defined by enclosing elements in curly braces {} or using set().
# They automatically remove duplicate values.

# Example of a set
my_set = {1, 2, 3, 4, 5}
print(f"My set: {my_set}")

# Set with mixed data types
mixed_set = {1, "Hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

# Creating an empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 3, 4}
print(f"Set with duplicates removed: {duplicate_set}")

# Most used methods of tuple in Python

# 1. count() - returns the number of times a value appears in a tuple
my_tuple = (1, 2, 2, 3, 2, 4, 2)
my_tuple = ("apple", "banana", "apple", "orange", "banana", "apple")
count_twos = my_tuple.count(2)  # 3
print(f"Count of 2s: {count_twos}")

# 2. index() - returns the index of the first occurrence of a value
index_of_three = my_tuple.index(3)  # 2
index_of_two  = my_tuple.index(2)  # 2
print(f"Index of 3: {index_of_three}")
print(f"Index of 2: {index_of_two}")

# 3. len() - returns the number of elements in a tuple
length = len(my_tuple)  # 6
print(f"Length: {length}")

# 4. min() - returns the smallest element
smallest = min(my_tuple)  # 1
print(f"Min: {smallest}")

# 5. max() - returns the largest element
largest = max(my_tuple)  # 4
print(f"Max: {largest}")

# 6. sum() - returns the sum of all elements
total = sum(my_tuple)  # 16
print(f"Sum: {total}")

# 6a. Calculate average marks of 10 students using tuple
student_marks = (85, 92, 78, 88, 95, 81, 89, 76, 90, 87)
average = sum(student_marks) / len(student_marks)
print(f"Average marks: {average:.2f}")

# 7. Unpacking - assign tuple elements to variables
c = 0
a, b,c = (10, 20, 30)
print(f"Unpacked: a={a}, b={b}, c={c}")

# 8. Slicing - extract a portion of a tuple
slice_tuple = my_tuple[1:4]  # (2, 3, 2)
print(f"Slice: {slice_tuple}")

# # 9. Concatenation - combine two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
print(f"Concatenated Tuple: {combined_tuple}")

my_tuple[1] = 5  # This will raise a TypeError because tuples are immutable

# A tuple is a collection of ordered, immutable elements in Python.
# Tuples are defined by enclosing elements in parentheses ().
# They can contain elements of different data types.

# Example of a tuple
my_tuple = (1, "Hello", 3.14, True) 

# Accessing elements in a tuple
first_element = my_tuple[0]  # 1
second_element = my_tuple[1]  # "Hello"

print(f"the fist element of my tupple is {first_element} and second element of my tupple is {second_element}")