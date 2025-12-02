## concatenate given lists to single list
lst1 = ['Hello', 'world', 'from', 'Python']
lst2 = [1, 2, 3, 4]
lst3 = ['This', 'is', 'a', 'test']

cl1 = lst1 + lst2 + lst3
cl2 = [*lst1, *lst2, *lst3]

print(cl1)
print(cl2)