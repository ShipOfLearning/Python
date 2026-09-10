## @ShipOfLearning (Day 43 of 100)
##  While loop
attempt = 0
while attempt < 3:
    pin = input("Enter your Pin : ") 
    if pin == "1234":
        print("Access Grant")
        break
    else:
        print("Wrong Pin ")
        attempt += 1
else:
    print("Card Blocked")
    