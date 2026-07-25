# Find First and Last Element of the list
lst = [6,4,5,8,7,2]
fe = lst[0]
le = lst[-1]
print(f"First Element: {fe} and last element is {le}")
fe,*rst,le =lst
print(f"First Element: {fe} lst as {rst} and last element is {le}")