import random

mylist = []
shuffled = []

for i in range(50):
    mylist.append(i)

for i in range(len(mylist) - 1):
    lenght = len(mylist)
    index = random.randint(0, lenght-1)
    shuffled.append(mylist.pop(index))

print(shuffled)