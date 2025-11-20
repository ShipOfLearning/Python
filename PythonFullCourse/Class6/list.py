# list comprehention
lst = [x for x in range(1,11)]
print(lst)
filtered_list = [x for x in lst if x % 2 == 0]
print(filtered_list)

filtered_list[0] = 110
print(filtered_list)

lst = [1,2,3,4,5,6,7,8,9,10]
print("reversed list:", lst[::-1])

# Most Used List Methods in Python

# append() - Add single element to end
lst = [1, 2, 3, 4, 5, 6,1,2,3]
print("Original List:", lst)
lst.append(4)  # [1, 2, 3, 4]
print("After append(4):", lst)

# extend() - Add multiple elements
list = [11, 12, 13, 14]
list.extend(lst) 
print("Extended List:", list)
lst.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
print("After extend([5, 6]):", lst)

# insert() - Add element at specific index
lst.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
print("After insert(0, 0):", lst)

# remove() - Remove first occurrence of value
lst.remove(0) 
print("After remove(0):", lst)
lst. remove(1)
print("After remove(1):", lst)

# pop() - Remove and return element at index
last = lst.pop()  # Returns 6
print("After pop():", lst, "Popped Element:", last)
middle = lst.pop(2)  # Returns 3
print("After pop(2):", lst, "Popped Element:", middle)

# index() - Find first occurrence of value
idx = lst.index(1)  # Returns 2
print("Index of first occurrence of 1:", idx)

# count() - Count occurrences of value
lst = [1, 2, 2, 3, 2]
print("List for count():", lst)
c = lst.count(2)  # Returns 3
print("Count of 2 in list:", c)

# sort() - Sort list in place
lst = [3, 1, 4, 2, 5]
print("Original List for sort():", lst)
lst.sort()  # Ascending order
print("After sort():", lst)
lst.sort(reverse=True)  # Descending order
print("After sort(reverse=True):", lst)

# reverse() - Reverse list in place
lst = [3, 2, 2, 5, 4]
lst.sort()
lst.reverse()
print("After reverse():", lst)

# copy() - Create shallow copy
lst_copy = lst.copy()
print("Original List:", lst)
print("Copied List:", lst_copy)
lst_copy.clear()
print("Original List:", lst)
print("Copied List:", lst_copy)

list1 = ["KiranKumar","Akhil","Ravi","Suresh"]
list2 = [2,3,4]
print(list1 + list2)


# clear() - Remove all elements
lst.clear()
lst = []
print(lst)

n_list  = [1,2,3,4]
print(n_list)

#Mix Datatype
mix_list = ["KiranKumar",12,12.45,[1,2,3]]
print(mix_list)

#List INdexing
list1 = ["KiranKumar",12,12.45,[1,2,3]]
print(list1[0])        #KiranKumar
print(list1[3])        #[1,2,3]
print(list1[4])     #2

list_numbers = [1,2,3,4,5,6,7,8,9,10]
print(list_numbers[-1])   

#List Slicing
list_numbers = [1,2,3,4,5,6,7,8,9,10]
print(list_numbers[0:5]) 
print(list_numbers[:3]) 
print(list_numbers[5:])
print(list_numbers[::2])

