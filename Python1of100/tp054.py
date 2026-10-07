## @ShipOfLearning (Day 54 of 100)
## Lambda Funcation

def sqr(x):
    return x*x

print(sqr(5))

sqr1 = lambda x : x*x
print(sqr1(5))

student = [("KK",41),("Malhar",18),("Amit",25)]
new_studer = sorted(student, key= lambda stud : stud[1])
print(new_studer)