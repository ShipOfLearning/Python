# ZIP
names = ["Rahul", "Amit", "Neha"]
scores = [90, 85, 95]

# for i in range(len(names)):
#     print(names[i], scores[i])

for name,score in zip(names,scores):
    print(name, score)