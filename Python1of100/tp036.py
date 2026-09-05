## @ShipOfLearning (Day 36 of 100)
## Nested Dictionary

student = {
    "S101" : {"name" : "KK", "marks": {"math" : 90, "hindi" : 85}},
    "S102" : {"name" : "Khiaan","marks": {"math" : 50, "hindi" : 75}}
}
print(student["S101"]["name"])
print(student["S101"]["marks"]["math"])
print(student.get("S101"))
print(student.get("S101").get("marks",{}))
print(student.get("S101").get("marks",{}).get("math"))