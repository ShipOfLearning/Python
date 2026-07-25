# try except
try:
    n = int(input("Enter a number: "))
    print(f"the squere of the number is {n * n}")
except ValueError:
    print("Please enter valid number")