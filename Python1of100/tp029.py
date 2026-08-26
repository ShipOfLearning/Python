## @ShipOfLearning (Day 29 of 100)
## Tuple Packing UnPacking

student = 25, "KK", "UAE"
print(student)
print(type(student))

# age, name, location =student
# print(f"age:{age}, name:{name}, location:{location}")

age, _, location =student
print(f"age:{age}, location:{location}")