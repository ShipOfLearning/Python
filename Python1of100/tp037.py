## @ShipOfLearning (Day 36 of 100)
## Dictionary Comprehension

marks = {"Aman": 30, "Riya": 88, "Kabir": 45}

result = {n : ("Pass" if m >= 40 else "Fail") \
    for n,m in marks.items()}
print(result)
