## @ShipOfLearning (Day 52 of 100)
## **kwargs Paramter

def user_infor(name, **kwargs):
    print(f"Name {name}")
    for k, v in kwargs.items():
        print(f"Key {k}, Value {v}")
        
user_infor("KK", address = "Ahmedabad")
user_infor("KK", address = "Ahmedabad",email = "KK@gmail.com")