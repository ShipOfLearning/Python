# *args
def avarage (*args):
    return sum(args) / len(args)

print(avarage(1, 2, 3, 4, 5))
print(avarage(1, 2, 3))