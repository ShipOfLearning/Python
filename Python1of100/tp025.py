## @ShipOfLearning
## List Comprehension (Day 25 of 100)

squares = []
for x in range(5):
    squares.append(x*x)
    
sq = [x*x for x in range(5)]

print(squares)
print(sq)

even_num = [x for x in range(20) if x % 2 == 0]
print(even_num)

num = [x for x in range(10) if x != 5]