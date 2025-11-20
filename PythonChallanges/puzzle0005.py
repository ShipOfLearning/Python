# lst = [2,9,5,8,1,4,7,6,3,0,9,9]
# second_highest = 8
numbers = [2,9,5,8,1,4,7,6,3,0,9,9]
numbers = list(set(numbers))
numbers.sort()
print(numbers[-2])
