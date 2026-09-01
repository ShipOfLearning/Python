## @ShipOfLearning (Day 34 of 100) (Part 2)
## Dictionary Methods Update(), Pop, PopItem(), copy()

student = {"name": "Aman", "age": 22, "city": "Delhi"}
print(student.update({"Maths" : 66}))
print(student)
val= student.pop("name")
print(val)
print(student)
print(student.popitem())
student1 = student.copy()

print(f"stu1 {student1}")