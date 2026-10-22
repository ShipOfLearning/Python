## @ShipOfLearning (Day 64 of 100)
## Sorted Methos

employees = [
    {"name": "Amit", "salary": 70000},
    {"name": "Neha", "salary": 50000},
    {"name": "Rahul", "salary": 90000}
]

lst = sorted(employees, key= lambda emp : emp["salary"], 
                reverse= True)
print(employees)
print(lst)