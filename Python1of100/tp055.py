## @ShipOfLearning (Day 55 of 100)
## Recursive Funcations

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))
