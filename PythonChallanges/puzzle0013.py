# Check if a list contains any duplicates
lst = [11,4,5,6,7]
if len(lst) != len(set(lst)):
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")