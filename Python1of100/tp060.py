## @ShipOfLearning (Day 60 of 100)
## Filter Funcation

orders = [100,2525,3000,450,600]
lst = list(filter(lambda x :  x> 1000,orders))

print(lst)

nl = [0,"",None,22]

lst = list(filter(None,nl))

print(lst)