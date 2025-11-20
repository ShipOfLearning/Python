# list = [1,2,3,4,5,6,7,8,9,10]
# Expected result: [2,4,6,8,10]

list = [1,2,3,4,5,6,7,8,9,10]
even = [num for num in list if num % 2 == 0]
print(even)
