a = "Python"
b = a
a += " Rocks"

print(b)
print(f"id of a: {id(a)}")
print(f"id of b: {id(b)}")

#reason: Strings are immutable in Python. When we do a += " Rocks", it creates a new string object and assigns it to 'a', while 'b' still references the original string "Python". Thus, 'b' remains unchanged.
#explaination : The code demonstrates the immutability of strings in Python. When we modify 'a' by appending " Rocks", it does not change the original string but creates a new string object. Therefore, 'b' still points to the original string "Python". The IDs printed confirm that 'a' and 'b' reference different objects after the modification.
#output: Python