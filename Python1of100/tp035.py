## @ShipOfLearning (Day 35 of 100)
## Loop Through Dictionary

student_marks = {"Amit": 85, "Riya": 92, "John": 78}

# for names in student_marks:
#     print(names)
    
for val in student_marks.values():
    print(val)
    
for names, val in student_marks.items():
    print(names, val)