## @ShipOfLearning (Day 31 of 100)
## Set Operations (Union, Intersection, Difference, Symmetric)

friends1 = {"Amit", "Neha", "Ravi", "Sanjay"}
friends2 = {"Malhar", "Neha", "Ravi", "Khiaan"}

print(friends1 | friends2)
print(friends1.union(friends2))

print(friends1 & friends2)
print(friends1.intersection(friends2))

print(friends1 - friends2)
print(friends2.difference(friends1))

print(friends1 ^ friends2)
print(friends1.symmetric_difference(friends2))