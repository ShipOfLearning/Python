## @ShipOfLearning (Day 54 of 100)
## enumerate()

lst = ["KK","Malhar","Khiaan"]

# index = 0
# for index in range(len(lst)):
#     print(index,lst[index])
#     index += 1

for index, value in enumerate(lst, start= 11):
    print(index, value)