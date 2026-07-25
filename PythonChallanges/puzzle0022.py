## Recursion in Python 

def countdown(n):
    if n == 0:
        # print("Done")
        return

    print(n)
    countdown(n - 1)

countdown(5)