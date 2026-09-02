## @ShipOfLearning
## Find nth Highest number from the list

def find_nth_highest_sort(numbers, n):
    arr = numbers[:]
    arr.sort(reverse = True)
    return arr[n-1]

def find_nth_highest_sorted(numbers, n):
    arr = sorted(numbers,reverse= True) 
    return arr[n-1]

def find_nth_highest(numbers, n):
    arr = numbers[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
    return arr[n-1]

lst = [5, 13, 56, 99, 43, 89]
n = 2

resulst = find_nth_highest_sort(lst,n)
print(f"the {n} highest number from {lst} is {resulst}")

resulst = find_nth_highest_sorted(lst,n)
print(f"the {n} highest number from {lst} is {resulst}")

resulst = find_nth_highest(lst,n)
print(f"the {n} highest number from {lst} is {resulst}")