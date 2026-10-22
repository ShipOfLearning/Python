## @ShipOfLearning (Day 54 of 100)
## Global vs Local Variables

balance = 1000

def update_blance():
    global balance
    balance = 500
    # print(balance)
    
update_blance()
print(balance)