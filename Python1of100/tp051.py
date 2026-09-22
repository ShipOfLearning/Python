## @ShipOfLearning (Day 51 of 100)
## *args Paramter

def add_num(*args,a,b,):
    restult = 0
    for a in args:
        restult += a
    return restult
        
val = add_num(1,2,3,4,5)
print(val)
